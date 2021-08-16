[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

## Install

### Without docker

#### Local

pip install -r requirements/local.txt

#### Production

pip install -r requirements/production.txt

### With docker

#### Local

docker-compose -f docker-compose-local.yml up -d --build

#### Production

compose/production/fastapi/Dockerfile
kubernetes.yaml

or

docker-compose -f docker-compose-production.yml up -d --build

## Docs

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

## Helping docs

https://gist.github.com/akshaybabloo/2a1df455e7643926739e934e910cbf2e

## CI

".pre-commit-config.yaml"
pre-commit run --all-files
pre-commit install

.github/workflows/test_code.yml

## TODO

- [ ] Add different responses for exceptions (resolver.NoAnswer, resolver.NXDOMAIN)
- [ ] Add other types of records
