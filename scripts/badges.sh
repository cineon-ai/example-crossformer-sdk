#!/bin/bash

# Ensure that the script exits if any commands fail
set -euo pipefail

## --- Generate release version badge ---
VERSION_BADGE=badges/version.svg
uv run scripts/badges/version.py --output-file $VERSION_BADGE

## --- Generate code coverage badge ---
COVERAGE_FILE=coverage.xml
COVERAGE_BADGE=badges/coverage.svg
uv run coverage xml -o $COVERAGE_FILE
uv run genbadge coverage \
    --input-file $COVERAGE_FILE \
    --output-file $COVERAGE_BADGE
rm $COVERAGE_FILE

## --- Generate complexity badge ---
COMPLEXITY_FILE=.complexity
COMPLEXITY_BADGE=badges/complexity.svg
uv run radon cc src/**/*.py -a >$COMPLEXITY_FILE
uv run scripts/badges/complexity.py \
    --input-file $COMPLEXITY_FILE \
    --output-file $COMPLEXITY_BADGE
