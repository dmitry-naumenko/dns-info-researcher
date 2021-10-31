mypy .
pytest .
flake8
coverage run --source='.' -m pytest
coverage-badge -f -o coverage.svg
