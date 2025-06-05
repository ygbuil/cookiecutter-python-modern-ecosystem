"""Sync files."""

import shutil
from pathlib import Path

import click
from loguru import logger


@click.command()
def sync_files() -> None:
    """Sync .pre-commit-config.yaml and .devcontainer/ from base repo into current project."""
    _sync_files()


def _sync_files() -> str:
    target_dir = Path.cwd()
    base_dir = Path(__file__).resolve().parent.parent / "sync_files"

    logger.info(f"Target project: {target_dir}")
    logger.info(f"Source template files: {base_dir}")

    # Copy .pre-commit-config.yaml
    source_precommit = base_dir / ".pre-commit-config.yaml"
    dest_precommit = target_dir / ".pre-commit-config.yaml"

    if source_precommit.exists():
        shutil.copy(source_precommit, dest_precommit)
        logger.success("Copied .pre-commit-config.yaml")
    else:
        logger.warning(".pre-commit-config.yaml not found in sync_files/")

    # Copy .devcontainer directory
    source_devcontainer = base_dir / ".devcontainer"
    dest_devcontainer = target_dir / ".devcontainer"

    if source_devcontainer.exists():
        shutil.copytree(source_devcontainer, dest_devcontainer, dirs_exist_ok=True)
        logger.success("Copied .devcontainer/")
    else:
        logger.warning(".devcontainer/ not found in sync_files/")

    return "Done."
