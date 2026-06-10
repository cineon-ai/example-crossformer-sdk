# Python repository template

![Latest Release](badges/version.svg) ![Coverage Status](badges/coverage.svg) ![Code complexity](badges/complexity.svg)

This serves as an example of how to set up a new Python project with:

    - A standard directory structure
    - A Python environment managed by `uv`
    - An example script: `scripts/example.py`
    - Semantic versioning
    - Formatting checks: `bash`; `markdown`
    - Python checks: `isort`; `ruff`; `mypy`
    - A testing suite
    - Badge generation
    - GitHub continuous integration that checks formatting and tests

You should update this `README` to be specific to your project. You should also update:

- The `[project]: name` field of `pyproject.toml`.
- The `[project]: description` field of `pyproject.toml`.
- The name of the `src/repository_template` directory.
- The name of the `src/repository_template/main.py` file.
- The string in `metadata.version` in `src/repository_template/version.py`

## Run the example

A simple "Hello World" example can be run using:

```bash
uv run scripts/example.py
```

## Set up the hooks

These pre-push hooks ensure that the formatter is run and the badges are updated every time you attempt to `git push`. This way formatting errors are caught and be corrected before they reach the GitHub continuous-integration (CI) step. The badges are then automatically up-to-date.

```bash
git config --local core.hooksPath .githooks/
```

## Check the formatting

The formatting can be checked manually using:

```bash
./scripts/format.sh
```

this is exactly the script that is run in the CI pipeline and the pre-push hook. Formatting uses `Prettier` for markdown, `shfmt` for shell scripts, and `ruff` for Python.

## Run the tests

The tests can be run manually using:

```bash
./scripts/test.sh
```
