"""Entry point for _say_hello()."""

import click
from loguru import logger


@click.command()
@click.option("--name")
@click.option("--surname")
def say_hello(name: str, surname: str) -> None:
    """Entry point to say hello.

    Args:
        name: Name.
        surname: Surname.

    Returns:
        Greet.
    """
    _say_hello(name, surname)


def _say_hello(name: str, surname: str) -> str:
    """Say hello to user.

    Args:
        name: Name.
        surname: Surname.

    Returns:
        Greet.
    """
    greet = f"Hello {name} {surname}!"
    logger.info(greet)

    return greet
