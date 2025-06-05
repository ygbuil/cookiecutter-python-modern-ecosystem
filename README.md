# Initial Repository Template

A description of the project

## Usage (with VSCode)

To use the project, follow these steps:

1. Install cookicutter in your machine with your desired package manager. Example: `uv add cookiecutter`.

2. On the directory you want to start a new Python project, type `cookiecutter gh:ygbuil/Init-Repo-Template-Uv`. You will be prompted with defining `project_slug`, which will be you project name in snakecase.

3. Open the project in VSCode, and you will be prompted with `Dev Containers: Reopen in Container`. Do that, and you will have a fully functional Python development environment.

## UV useful commands

* `uv run <command>`: Run any command within the venv interpreter space.
* `uv sync`: Install dependencies based on `uv.lock`. If not found, it will create a new lock with the latest dependencies possible.
* `uv lock`: Update `uv.lock` based on `pyproject.toml` specifications.
