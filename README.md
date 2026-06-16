# Crossformer Example Repository

![Latest Release](badges/version.svg) ![Coverage Status](badges/coverage.svg) ![Code complexity](badges/complexity.svg)

This repository contains an example of how to use the crossformer binary. For convenience a class, `CrossformerModel`, has been provided that provides type hints, but is in no way required to use the `crossformer_binary_sdk`.

## Installation

The `crossformer_binary_sdk` only provides part of the required code to run a crossformer. The model weights and architecture must also be provided, as well as a set of configuration files. These will be shared with users of this repository, and should be placed in a directory `model/` by default.

Start by installing this package's dependencies, then the model-specific dependencies. Make sure to do this in the order below, as `uv sync` removes packages from the virtual environment it doesn't see in the `pyproject.toml`.

```bash
uv sync
uv pip install crossformer_binary_sdk-<version>-<arch>.whl
```

Check the installation worked as expected by running the following:

```bash
uv run python -c "from cineon_sdk import crossformer_binary_sdk;print(crossformer_binary_sdk)"
```

Which should print something like `<module 'cineon_sdk.crossformer_binary_sdk' from '.venv/Lib/site-packages/cineon_sdk/crossformer_binary_sdk.pyd'>`

## Run the notebook

In `notebooks/` there is a python notebook, `test_sdk.ipynb`, which contains an example showing how to load the model, as well as how to preprocess data, and what the predictions look like from the model.

## Run the tests

The tests can be run manually using:

```bash
./scripts/test.sh
```
