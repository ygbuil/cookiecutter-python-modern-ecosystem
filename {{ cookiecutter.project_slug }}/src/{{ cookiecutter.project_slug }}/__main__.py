"""Cli."""

import click

from {{ cookiecutter.project_slug }} import cli


def _main() -> None:
    """Adds all cli commands."""

    @click.group(chain=True)
    def add_cli_command() -> None:
        """Adds a cli command."""

    for command in (cli.say_hello,):
        add_cli_command.add_command(command)

    add_cli_command()
