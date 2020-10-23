# -*- coding: utf-8 -*-

import os
import json
from pprint import pprint
from collections import OrderedDict

import click
import pefile


def find_dll_dependencies(dll_filepath, dll_dir, dependencies=None):
    if dependencies is None:
        dependencies = OrderedDict()

    pe_file = pefile.PE(dll_filepath)
    pe_name = os.path.basename(dll_filepath)

    if pe_name not in dependencies:
        dependencies[pe_name] = []

    for entry in pe_file.DIRECTORY_ENTRY_IMPORT:
        entry_name = entry.dll.decode("utf-8")
        if entry_name not in dependencies[pe_name]:
            dependencies[pe_name].append(entry_name)
        if entry_name in os.listdir(dll_dir):
            find_dll_dependencies(os.path.join(dll_dir, entry_name), dll_dir, dependencies)

    return dependencies


@click.command("pedep")
@click.argument("filepath")
@click.option("-d", "--dll-dir")
@click.option("-j", "--json", is_flag=True)
@click.pass_context
def cli(*args, **kwargs):
    """List PE file dependencies."""
    filepath = kwargs["filepath"]
    json_output = kwargs["json"]
    dll_dir = kwargs["dll_dir"]

    if dll_dir is None:
        pe_file = pefile.PE(filepath)
        pe_name = os.path.basename(filepath)

        dependencies = {}
        dependencies[pe_name] = []

        for entry in pe_file.DIRECTORY_ENTRY_IMPORT:
            entry_name = entry.dll.decode("utf-8")
            dependencies[pe_name].append(entry_name)
    else:
        dependencies = find_dll_dependencies(filepath, dll_dir)

    if not json_output:
        for k, v in dependencies.items():
            click.echo(f"Imports for {k}:")
            for entry in v:
                click.echo(f"  - {entry}")
            click.echo()
    else:
        click.echo(json.dumps(dependencies, indent=4))
