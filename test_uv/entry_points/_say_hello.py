"""Entry point for _say_hello()."""

import click
from loguru import logger


@click.command()
@click.option("--name")
@click.option("--surname")
def say_hello(name: str, surname: str) -> str:
    """Entry point to say hello.

    :param name: Name.
    :param surname: Surname.
    :return: Greet.
    """
    return _say_hello(name, surname)


def _say_hello(name: str, surname: str) -> str:
    """Say hello to user.

    :param name: Name.
    :param surname: Surname.
    :return: Greet.
    """
    greet = f"Hello {name} {surname}!"
    logger.info(greet)

    return greet
