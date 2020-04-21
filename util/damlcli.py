#!/usr/bin/env python

import sys
import os
import importlib
import itertools
import click
from mypublib import nbops


@click.group()
@click.option('-d', '--debug', is_flag=True, help='Debug mode of commands.')
@click.pass_context
def cli(ctx, debug):
    ctx.ensure_object(dict)
    base = os.path.dirname(sys.path[0])
    ctx.obj['BASEDIR'] = base
    ctx.obj['DEBUG'] = debug
    if debug:
        click.echo(f'Publish CWD: {base}')


@cli.command()
@click.argument('nbinput', type=click.File('r'))
@click.argument('nboutput', type=click.File('w'))
@click.pass_context
def clearnb(ctx, nbinput, nboutput):
    """
    Clears all outputs in the notebook.
    """
    if ctx.obj['DEBUG']:
        click.echo(f'Clear notebook: {nbinput.name} -> {nboutput.name}')
    nbops.clearnb(nbinput, nboutput)


@cli.command()
@click.option(
        '-s', '--slides', is_flag=True, help='Slides HTML, no div borders.')
@click.option('-f', '--imgfmt', default='b64', help='Attached image format.')
@click.argument('nbinput', type=click.File('r'))
@click.argument('htmlout', required=False)
@click.pass_context
def exporthtml(ctx, slides, imgfmt, nbinput, htmlout):
    """
    Exports complete HTML, including attachments.

    Either as notebook HTML or slides (full horizontal space) HTML.
    """
    if not htmlout:
        base, _ = os.path.splitext(os.path.basename(nbinput.name))
        htmlout = f'{base}.html'
    htmlout = open(htmlout, 'w')
    if ctx.obj['DEBUG']:
        if slides:
            click.echo(f'Export slides HTML: {nbinput.name} -> {htmlout.name}')
        else:
            click.echo(f'Export full HTML: {nbinput.name} -> {htmlout.name}')
    nbops.html_export(nbinput, htmlout, imgfmt=imgfmt, slides=slides)


AVAILABLE_BUILDS = ['city']
def list_builds(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    for build in AVAILABLE_BUILDS:
        click.echo(build)
        mod = importlib.import_module('.'.join(['mypublib', build]))
        builddef = mod.BUILD
        for k in sorted(builddef.keys()):
            click.echo(f'    {k}')
            for i in builddef[k]:
                click.echo(f'        {i}')
    ctx.exit()


@cli.command()
@click.option('-l', '--list', is_flag=True, help='List all builds and exit.',
              expose_value=False, is_eager=True, callback=list_builds)
@click.option('-n', '--dry-run', is_flag=True, help='Only print the actions.')
@click.argument('build')
@click.argument('part', required=False)
@click.pass_context
def buildpub(ctx, dry_run, build, part):
    """
    Builds a specific publication

    Or a specific part of a specific publication.
    The special option `--list` outputs the available builds.
    """
    mod = importlib.import_module('.'.join(['mypublib', build]))
    builddef = mod.BUILD
    if part:
        tasks = builddef[part]
    else:
        tasks = itertools.chain(*builddef.values())
    os.chdir(ctx.obj['BASEDIR'])
    for t in tasks:
        if dry_run or ctx.obj['DEBUG']:
            click.echo(t)
        if not dry_run:
            t.publish()


if '__main__' == __name__:
    cli(obj={})

