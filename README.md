# Example Crossformer Repository

![Latest Release](badges/version.svg) ![Coverage Status](badges/coverage.svg) ![Code complexity](badges/complexity.svg)

This repository contains an example of how to use Cineon Crossformer binaries. For convenience a wrapper Python class, `CrossformerModel`, has been provided that provides type hints, but this is in no way required to use the binaries.

## Installation

This repository only provides part of the required code to run a binary. The weights and architecture must also be provided, together with a set of configuration files. These will be shared separately with users of this repository. The binary wheel should be placed in the root directory of the repository and the model files should be placed in the `model/` directory.

The installation requires the Python package manager `uv`. This is provided in the Docker image `quay.io/pypa/manylinux_2_28_x86_64`.

By default, when interacting with `uv` it will try and remove packages installed in the virtual environment that are not present in `pyproject.toml`. This is an issue because we have some model-specific dependencies not present in `pyproject.toml`, so care must be taken not to `uv sync` or `uv run` when the model dependencies are installed.

First install the package dependencies:

```bash
uv sync
```

After installing the package dependencies, install the model-specific dependencies:

```bash
uv pip install -r model/requirements.txt
```

Make sure to do these commands in that specific order since `uv sync` removes packages from the virtual environment that it does not see in the `pyproject.toml`.

The best way to not face issues is to activate the virtual environment in `.venv` with the following command. This command should be ran before continuing.

```bash
source .venv/bin/activate
```

Check the installation works as expected by running the following command:

```bash
python -c "from cineon_sdk import crossformer_binary_sdk;print(crossformer_binary_sdk)"
```

which should print something like:

```text
<module 'cineon_sdk.crossformer_binary_sdk' from '.venv/Lib/site-packages/cineon_sdk/crossformer_binary_sdk.abi3.so'>
```

and then run the tests:

```bash
pytest ./tests
```

## Run the notebook

In `notebooks/` there is a python notebook, `demo.ipynb`, which contains an example showing how to load the model and data, as well as how to preprocess data, and what the predictions look like from the model.
