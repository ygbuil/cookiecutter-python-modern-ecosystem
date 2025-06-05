"""Entry points for initial_repository_template."""

import click

from init_repo_template_uv import entry_points


def _main() -> None:
    """Gathers all entry points of the program."""

    @click.group(chain=True)
    def entry_point() -> None:
        """Entry point."""

    for command in (entry_points.say_hello, entry_points.sync_files):
        entry_point.add_command(command)

    entry_point()
