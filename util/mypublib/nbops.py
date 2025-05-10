#!/usr/bin/env python

import os
import shutil
import click
import nbformat
import nbconvert

def clearnb(f_in, f_out):
    """
    Clears all output within a notebook.

    This pretty much does tha same as:

        jupyter-nbconvert --to=notebook \
                          --ClearOutputPreprocessor.enabled=True \
                          --output=open(f_out) \
                          --output-dir=<...> \
                          f_in
    """
    notebook = nbformat.read(f_in, as_version=4)
    clear_prep = nbconvert.preprocessors.ClearOutputPreprocessor()
    clear_nb, _ = clear_prep.preprocess(notebook, None)
    nbformat.write(clear_nb, f_out)


class Exp(nbconvert.SlidesExporter):
    pass
    #template_file = 'basic.tpl'
    #template_file = '/home/grochmal/programs/my/daml/basic.tpl'
    #default_template_path = '/home/grochmal/programs/my/daml'
    #default_template_path = os.path.join("..", "templates", "html")
    #def _template_file_default(self):
    #    return 'basic.tpl'


def html_export(nbin, htmlout, imgfmt='b64', slides=False):
    """
    Does a complete HTML export, including cell attachments.

    Function heavily inpired by the code in the github issue:
    https://github.com/jupyter/nbconvert/issues/699
    by Søren Fuglede Jørgensen and Donghyun Kwak.
    """
    contents = nbin.read()
    # first convert it the normal way
    notebook = nbformat.reads(contents, as_version=4)
    if slides:
        exporter = nbconvert.SlidesExporter()
    else:
        exporter = nbconvert.HTMLExporter()
    #exporter = Exp()
    exporter = nbconvert.HTMLExporter()
    #exporter.template_file = '/home/grochmal/programs/my/daml/basic.tpl'
    exporter.template_file = '/home/grochmal/programs/my/daml/bookhtml.tpl'
    print('PATH', Exp.default_template_path)
    resources = {
        'title': 'NB Title',
        #'mathjax': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML'
        'mathjax': 'MathJax-2.7.5/MathJax.js?config=TeX-AMS_HTML',
        'main_style': 'bookhtml.css',
        'extra_style': None,
    }
    body, _ = exporter.from_notebook_node(notebook, resources=resources)
    # save a mapping of all attachments
    images = []
    for cell in notebook['cells']:
        if 'attachments' in cell:
            atts = cell['attachments']
            for filename, att in atts.items():
                for mime, base64 in att.items():
                    images.append({
                        'att_name': f'attachment:{filename}',
                        'name': f'{filename}',
                        'href': f'{filename}',
                        'b64': f'data:{mime};base64,{base64}',
                    })
    # fix the HTML by hand
    for i in images:
        att = i['att_name']
        data = i[imgfmt]
        body = body.replace(f'src="{att}"', f'src="{data}"', 1)
        short = data[:60]
        if len(data) > 60:
            short += '...'
        click.echo(f'Image at: src="{short}"')
    click.echo('%s %s' %  (dir(body), type(body)))
    click.echo(body[:200])
    htmlout.write(body)


class PublishFile(object):
    """
    Abstract data structure for operations from one file to another.

    Used to publish the `origin` file as the `destination` file.
    """
    action = 'Do nothing'

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    @classmethod
    def from_obj(cls, obj, ext=None):
        destination = obj.destination
        if ext:
            base, _ = os.path.splitext(obj.destination)
            destination = base + ext
        return cls(obj.origin, destination)

    def __str__(self):
        return f'{self.action} {self.origin} -> {self.destination}'


class ClearNotebook(PublishFile):
    """
    Data structure to hold notebook cleaning configuration.
    """
    action = 'Clear notebook'

    def publish(self):
        f_in = open(self.origin)
        os.makedirs(os.path.dirname(self.destination), exist_ok=True)
        f_out = open(self.destination, 'w')
        clearnb(f_in, f_out)


class ExportNotebook(PublishFile):
    """
    Data structure to hold notebook to HTML conversion.
    """
    action = 'Notebook to HTML'

    def publish(self):
        nbin = open(self.origin)
        os.makedirs(os.path.dirname(self.destination), exist_ok=True)
        htmlout = open(self.destination, 'w')
        html_export(nbin, htmlout, slides=True)


class CopyFile(PublishFile):
    """
    Polymorphic structure to simply copy a file.
    """
    action = 'Copy file'

    def publish(self):
        os.makedirs(os.path.dirname(self.destination), exist_ok=True)
        shutil.copyfile(self.origin, self.destination)


class SoftLink(PublishFile):
    """
    Data structure for softlinks (e.g. for data files).
    """
    action = 'Softlink'

    def publish(self):
        dirs = ['..'] * self.destination.count(os.path.sep) + [self.origin]
        origin = os.path.join(*dirs)
        os.makedirs(os.path.dirname(self.destination), exist_ok=True)
        try:
            os.unlink(self.destination)
        except FileNotFoundError:
            pass
        os.symlink(origin, self.destination)

