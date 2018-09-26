# Automation Scripts

The scripts in this directory make use of python's script import rules.
In other words, when one runs a python file as a script (instead of a package),
the following points can be assumed:

1.  The `sys.path` (i.e. `PYTHONPATH`) is populated with the containing
    directory of the script as its first component.  This works independently
of how the script is executed, e.g. from a completely different directory or
with an absolute path.  The first component of `sys.path` is used to find the
location of the repository on the filesystem.

2.  Importing though the `sys.path` can be performed as if packages have been
    installed into that directory.  In other words, any directories containing
python files in the place where the script lives can be imported directly as
packages (full import - not relative import which is forbidden in scripts).
Imports within the imported packages word as normal.  We use this behaviour to
store common code in the `mypublib` directory/package.

The above works in pretty much all instances of python invocation as a script.
For example, all the following ways of invoking `build-city.py` are valid,
and will execute imports in the correct order:

    ./build-city.py
    python build-city
    cd .. && python util/build-city.py
    cd .. && ln -s util/build-city.py build-city && ./build-city

The only thing one needs to be careful about is not to mix relative imports in
the package(s) with absolute imports into the scripts themselves.
If there is code that may need to be imported it needs to go into `mypublib`
(or another package if needed).
In the `util` directory itself, only entry-point scripts should live as regular
files.


## Requirements

Most script will be working with jupyter notebooks,
therefore the automation tools for jupyter are required:

- `nbconvert`
- `nbformat`

It is good to have the jupyter environment with most scientific packages at
hand, since some scripts will use at leasts parts of them:

- `jupyter-notebook`
- `ipython`
- `numpy`
- `matplotlib`
- `scipy`
- `pandas`

Also, the command line is parsed with:

- `click`

All these packages come with the default install of most scientific
distributions of python, notably anaconda.

