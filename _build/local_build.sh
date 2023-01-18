#!/bin/zsh
set -e

echo "Installing files"
poetry install --no-interaction

echo "Generate files"
find src/ -type f -name '*.pyi' -exec rm {} +
stubgen src/ -o src/

echo "Running mypy"
mypy src/ --strict
mypy tests/ --strict
echo "\nRunning flake8"
flake8 --max-line-length 120 src/
flake8 --max-line-length 120 tests/
echo "\nRunning black"
black src/ -l 120 --check
black tests/ -l 120 --check

echo "\nRunning Unit Tests"
pytest  --cov-branch --cov=src/ tests/ --log-cli-level=DEBUG --junit-xml=junit.xml --cov-report=xml --cov-report=html:ci_coverage/


echo "\n\nBuild completed successfully"