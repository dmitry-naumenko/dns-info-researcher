set -e

mypy .
pytest .
flake8
coverage run --source='.' -m pytest
coverage-badge -f -o .github/assets/coverage.svg
