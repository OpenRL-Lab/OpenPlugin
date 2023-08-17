#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2023 The OpenRL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""""""


import click
from click.core import Context, Option
from termcolor import colored

from openplugin import __AUTHOR__, __EMAIL__, __TITLE__, __VERSION__
from openplugin.utils.util import get_system_info


def red(text: str):
    return colored(text, "red")


def print_version(
    ctx: Context,
    param: Option,
    value: bool,
) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.secho(f"{__TITLE__.upper()} version: {red(__VERSION__)}")
    click.secho(f"Developed by {__AUTHOR__}, Email: {red(__EMAIL__)}")
    ctx.exit()


def print_system_info(
    ctx: Context,
    param: Option,
    value: bool,
) -> None:
    if not value or ctx.resilient_parsing:
        return
    info_dict = get_system_info()
    for key, value in info_dict.items():
        click.secho(f"- {key}: {red(value)}")
    ctx.exit()


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(invoke_without_command=True)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show package's version information.",
)
@click.option(
    "--system_info",
    is_flag=True,
    callback=print_system_info,
    expose_value=False,
    is_eager=True,
    help="Show system information.",
)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        pass
    else:
        pass
        # click.echo(f"I am about to invoke {ctx.invoked_subcommand}")


@cli.command()
@click.argument("plugin_name")
def install(plugin_name):
    from openplugin.install import install_plugin

    install_plugin(plugin_name)


@cli.command()
@click.argument("plugin_name")
def uninstall(plugin_name):
    from openplugin.install.uninstall import uninstall_plugin

    uninstall_plugin(plugin_name)


@cli.command()
@click.argument("plugin_name")
def reinstall(plugin_name):
    from openplugin.install import reinstall_plugin

    reinstall_plugin(plugin_name)


@cli.command()
def list():
    from openplugin.install.list_plugins import list_plugins

    list_plugins()


@cli.command()
@click.argument("plugin_name")
@click.option(
    "--host",
    type=str,
    default="0.0.0.0",
    help="Host to run the plugin.",
)
@click.option(
    "-p",
    "--port",
    type=int,
    default=5003,
    help="Port to run the plugin.",
)
def run(plugin_name, host, port):
    from openplugin.run import run_plugin

    run_plugin(plugin_name, host=host, port=port)
