#!/bin/bash

# Ensure that the script exits if any commands fail
set -euo pipefail

# Install dependencies
uv sync --locked --dev

# Run all tests
uv run coverage run -m pytest
uv run coverage report
