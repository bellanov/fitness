#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
uv run isort .

echo "Formatting code base..."
uv run black . 
