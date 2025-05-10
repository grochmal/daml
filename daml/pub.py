import os
import shutil
import contextlib
import zipfile
from dataclasses import dataclass
from functools import singledispatch
import nbformat
import nbconvert


@dataclass
class Directory:
    path: str


@dataclass
class Operation:
    ...


@dataclass
class ClearNotebook(Operation):
    source_f: str
    out_f: str
    out_dir: Directory


@dataclass
class CopyFile(Operation):
    source_f: str
    out_dir: Directory


@dataclass
class ZipDirectory(Operation):
    input_dir: Directory
    extensions: list[str] = (".ipynb", ".svg", ".csv", ".txt", ".png")


@contextlib.contextmanager
def ctx_cd(x):
    d = os.getcwd()
    os.chdir(x)
    try:
        yield
    finally:
        os.chdir(d)


@singledispatch
def perform_operation(op, nb_dir: str, pub_dir: str):
    raise ValueError(f"Opearion {op} not supported")


@perform_operation.register
def _(op: ClearNotebook, nb_dir: str, pub_dir: str):
    f_in = os.path.join(nb_dir, op.source_f)
    f_out = os.path.join(pub_dir, op.out_dir.path, op.out_f)
    os.makedirs(os.path.join(pub_dir, op.out_dir.path), exist_ok=True)
    with open(f_in) as in_f:
        with open(f_out, "w") as out_f:
            notebook = nbformat.read(in_f, as_version=4)
            clear_prep = nbconvert.preprocessors.ClearOutputPreprocessor()
            clear_nb, _ = clear_prep.preprocess(notebook, None)
            nbformat.write(clear_nb, out_f)


@perform_operation.register
def _(op: CopyFile, nb_dir: str, pub_dir: str):
    f_in = os.path.join(nb_dir, op.source_f)
    f_out = os.path.join(pub_dir, op.out_dir.path, op.source_f)
    os.makedirs(os.path.dirname(op.out_dir.path), exist_ok=True)
    shutil.copyfile(f_in, f_out)


@perform_operation.register
def _(op: ZipDirectory, nb_dir: str, pub_dir: str):
    in_dir = os.path.join(pub_dir, op.input_dir.path)
    dirname, basename = os.path.split(in_dir)
    out_f = f"{basename}.zip"
    with ctx_cd(dirname):
        with zipfile.ZipFile(out_f, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(basename):
                for f in files:
                    _, ext = os.path.splitext(f)
                    if ext not in op.extensions:
                        continue
                    zf.write(os.path.join(root, f))


def build_lecture(operations: list[Operation]):
    nb_dir = os.getenv("NB_DIR", "nb")
    pub_dir = os.getenv("PUB_DIR", "pub")
    for op in operations:
        perform_operation(op, nb_dir, pub_dir)
