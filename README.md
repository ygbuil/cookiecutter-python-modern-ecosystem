# Cookiecutter template for modern Python projects

A Cookiecutter template with the latest and best tools for python development, featuring:

* Devcontainer: Develop locally inside a Docker container for maximum reproducibility.
* Package manager: UV, developed by Astral. The fastest and most elegant way to manage Python versions, packages, virtual environments and builds.
* Pre commit:
    * Formatting and linting: Ruff, developed by Astral.
    * Static type checker: mypy.
    * Testing: Pytest
* CLI: Pre defined entry points using Click.

## Usage

The template you will get is based on the content inside `{{ cookiecutter.project_slug }}`. Ignore the rest of the code, it is for development.

To use the project, follow these steps:

1. Install cookicutter in your machine with your desired package manager. Example: `uv add cookiecutter`.
2. On the directory you want to start a new Python project, type `cookiecutter gh:ygbuil/Cookiecutter-Python-Modern-Ecosystem`. You will be asked to define `project_slug`, which is your project/package name in snakecase.
3. Open the project in VSCode, and you will be prompted with `Dev Containers: Reopen in Container`. Do that, and you will have a fully functional Python development environment.

## UV useful commands

* `uv run <command>`: Run any command within the venv interpreter space.
* `uv sync`: Install dependencies based on `uv.lock`. If not found, it will create a new lock with the latest dependencies possible.
* `uv lock`: Update `uv.lock` based on `pyproject.toml` specifications.

## (Ignore) Notes for me, the developer

Local workflow:
* Perform changes in the `{{ cookiecutter.project_slug }}`.
* To test the code, it will need to be parsed since it contains Jinja. To do so, use the `Compile cookiecutter template` command in `tasks.json`. This will create the parsed code in the root dir inside `my_package_name`.
* To execute the code, open `my_package_name` as a completly independent project in VSCode with its own environment, and execute there. 
