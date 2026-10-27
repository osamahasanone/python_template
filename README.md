# Python project template

A [Copier](https://copier.readthedocs.io) template for small Python projects to try things out, with uv, python-dotenv, ruff, ty, prek, pytest and IPython. No Docker: everything runs locally with `uv run`.

Only the `template/` folder is copied into new projects. This README and `copier.yml` stay here.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- [prek](https://github.com/j178/prek), for the Git hooks
- Git

## Create a new project

```bash
uvx copier copy --trust gh:osamahasanone/python_template ~/Desktop/my_project
```

Copier asks for:

- **Project name**: lowercase with underscores, e.g. `my_project`.
- **Description**: goes into `pyproject.toml`.
- **Python version**: press Enter to keep `3.14`. The same value is written to `pyproject.toml` and `.python-version`, so they always match.

`--trust` is needed because the template runs commands after copying the files. Those commands:

1. Run `git init`.
2. Install all packages with `uv add`, always the latest versions.
3. Install the prek Git hooks.
4. Run ruff to fix and format the code.

Then start the project:

```bash
cd ~/Desktop/my_project
uv run python main.py
uv run pytest
```

## What's in a new project

| File | Purpose |
|---|---|
| `pyproject.toml` | Project metadata, ruff and pytest settings |
| `main.py` | Starting point; reads `.env` with python-dotenv |
| `tests/test_main.py` | Example test |
| `.env` / `.env.example` | Real local values (never committed) / the list of variables to set (committed) |
| `prek.toml` | Checks that run on every commit |
| `.vscode/tasks.json` | Common commands via `Cmd + Shift + P` → Tasks: Run Task |
| `.copier-answers.yml` | Your answers, used by `copier update` |

## Change the template

1. Edit files in `template/`. Files ending in `.jinja` can use `{{ project_name }}`, `{{ description }}` and `{{ python_version }}`. Copier removes `.jinja` from their names.
2. Commit and tag a new version:
   ```bash
   git commit -am "Describe the change"
   git tag v1.1.0
   git push --follow-tags
   ```
3. Pull the change into an existing project (run inside that project, with its changes committed):
   ```bash
   uvx copier update --trust
   ```
