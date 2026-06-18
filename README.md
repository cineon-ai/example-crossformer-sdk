# Example Crossformer Repository

![Latest Release](badges/version.svg) ![Coverage Status](badges/coverage.svg) ![Code complexity](badges/complexity.svg)

This repository contains an example of how to use Cineon Crossformer binaries. For convenience a wrapper Python class, `CrossformerModel`, has been provided that provides type hints, but this is in no way required to use the binaries.

## Installation

This repository only provides part of the required code to run a binary. The weights and architecture must also be provided, together with a set of configuration files. These will be shared separately with users of this repository. The binary wheel should be placed in the `binary/` directory of the repository and the model files should be placed in the `model/` directory.

The installation requires the Python package manager `uv`. This is provided in the Docker image `quay.io/pypa/manylinux_2_28_x86_64`.

First install the package dependencies:

```bash
uv sync
```

After installing the package dependencies, install the model-specific dependencies:

```bash
uv pip install -r model/requirements.txt --index-strategy unsafe-best-match
```

We found it necessary to set an environment variable to prevent the install from timing out

```bash
export UV_HTTP_TIMEOUT=10000000
```

Make sure to do these commands in that specific order since `uv sync` removes packages from the virtual environment that it does not see in the `pyproject.toml`.

By default, `uv sync` (and commands like `uv run` that may sync the environment) will try to remove packages installed in the virtual environment that are not present in `pyproject.toml`. This is an issue because we have some model-specific dependencies not present in `pyproject.toml`, so care must be taken not to `uv sync` or `uv run` when the model dependencies are installed. Note carefully the use of `--no-sync` in the commands below.

Check the installation works as expected by running the following command:

```bash
uv run --no-sync python -c "from cineon_sdk import crossformer_binary_sdk;print(crossformer_binary_sdk)"
```

which should print something like:

```text
<module 'cineon_sdk.crossformer_binary_sdk' from '.venv/Lib/site-packages/cineon_sdk/crossformer_binary_sdk.abi3.so'>
```

## Run the tests

To run the testing suite:

```bash
uv run --no-sync pytest
```

## Run the example

To run the example:

```bash
uv run --no-sync src/example_crossformer_sdk/main.py
```

## Run the notebook

In `notebooks/` there is a python notebook, `demo.ipynb`, which contains an example showing how to load the model and data, as well as how to preprocess data, and what the predictions look like from the model.
