# Initial Repository Template

A description of the project

## Usage (with VSCode)

To use the project, follow these steps:

1. Clone the project.

2. Open the project and build the `.devcontainer/Dockerfile` with the VSCode command `Dev Containers: Reopen in Container`.

3. Inside `.vscode/tasks.json`, provide your inputs and run the VSCode command `Tasks: Run Task -> ...`.

## UV useful commands

* `uv run <command>`: Run any command within the venv interpreter space.
* `uv sync`: Install dependencies based on `uv.lock`. If not found, it will create a new lock with the latest dependencies possible.
* `uv lock`: Upgrade dependencies to the latest version possible.