#!/usr/bin/env bash

set -e
set -x

coverage run --source='.' -m pytest
coverage report --show-missing --fail-under=100
