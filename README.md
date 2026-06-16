# Crossformer Example Repository

![Latest Release](badges/version.svg) ![Coverage Status](badges/coverage.svg) ![Code complexity](badges/complexity.svg)

This repository contains an example of how to use Crossformer binaries. For convenience a wrapper class, `CrossformerModel`, has been provided that provides type hints, but is in no way required to use the `crossformer_binary_sdk`.

## Installation

The SDK only provides part of the required code to run a Crossformer. The weights and architecture must also be provided, together with a set of configuration files. These will be shared separately with users of this repository and should be placed in the `model/` directory by default.

The installation requires the Python package manager `uv`. This is provided in the Docker image `quay.io/pypa/manylinux_2_28_x86_64`.

Start by installing the package dependencies:

```bash
uv sync
```

followed by the model-specific dependencies:

```bash
uv pip install model/<name>-<version>-<arch>.whl
```

Make sure to do this in order since `uv sync` removes packages from the virtual environment that it does not see in the `pyproject.toml`.

Check the installation works as expected by running the following command:

```bash
uv run python -c "from cineon_sdk import crossformer_binary_sdk;print(crossformer_binary_sdk)"
```

Which should print something like: `<module 'cineon_sdk.crossformer_binary_sdk' from '.venv/Lib/site-packages/cineon_sdk/crossformer_binary_sdk.abi3.so'>`.

## Run the notebook

In `notebooks/` there is a python notebook, `demo.ipynb`, which contains an example showing how to load the model, as well as how to preprocess data, and what the predictions look like from the model.

## Run the tests

The tests can be run manually using:

```bash
./scripts/test.sh
```
