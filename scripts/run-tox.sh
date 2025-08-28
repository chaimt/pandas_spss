#!/bin/bash

# Script to run tox with common options
# Usage: ./scripts/run-tox.sh [environment] [additional_args]

set -e

# Default environment
ENV=${1:-"py313"}
shift || true

echo "Running tox environment: $ENV"
echo "Additional arguments: $@"

# Run tox with the specified environment and arguments
uv run tox -e "$ENV" "$@"
