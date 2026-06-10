#!/bin/bash

# Ensure that the script exits if any commands fail
set -euo pipefail

# Check the markdown formatting
npx prettier --check "**/*.md"

# Check the shell-script formatting
shfmt --diff --indent 4 scripts

# Install Python dependencies
uv sync --locked --dev

# Check the Python formatting
DIRECTORIES=("src/" "tests/" "scripts/")
uv run isort --check "${DIRECTORIES[@]}"
uv run ruff check "${DIRECTORIES[@]}"
uv run mypy "${DIRECTORIES[@]}" --follow-untyped-imports
