![coverage](.github/assets/coverage.svg)
![Tests](https://github.com/dmitry-naumenko/dns-info-researcher/workflows/Tests/badge.svg)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![wblack](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Dependabot Status](https://img.shields.io/badge/Dependabot-active-brightgreen.svg)](https://dependabot.com)

# DNS INFO RESEARCHER

Demo:
https://dns.madn.top/docs
https://dns.madn.top/redoc

## Table of Contents

- [Installation](#installation)
  - [Without docker](#without-docker)
  - [With docker](#with-docker)
- [Usage](#usage)
  - [URL](#url)
  - [Docs](#docs)

## Installation

Create .env file in project root and set environment variables for application (example: .env.example).

#### Without docker

Install requirements:

Local verision:
`pip install -r requirements/local.txt`
Production version:
`pip install -r requirements/production.txt`

To run the web application:
`uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

#### With docker

You must have docker and docker-compose tools installed to work with material in this section.

Local verision:
`docker-compose -f docker-compose-local.yml up -d --build`
Production version:
`docker-compose -f docker-compose-production.yml up -d --build`
or use kubernetes.yaml

#### Kubernetes

Use kubernetes.yaml and autoscale.yaml

## Usage

### URL

Application will be available on localhost in your browser.

### Docs

All routes are available on /docs or /redoc paths with Swagger or ReDoc.

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

## Run tests

`bash start_all_tests.sh`

## Business logic docs

https://gist.github.com/akshaybabloo/2a1df455e7643926739e934e910cbf2e

## Project structure

Files related to application are in the app or tests directories. Application parts are:

```
app
├── api              - web related stuff.
│   ├── dependencies - dependencies for routes definition.
│   ├── errors       - definition of error handlers.
│   └── routes       - web routes.
├── core             - application configuration, startup events, logging.
├── db               - db related stuff.
│   ├── migrations   - manually written alembic migrations.
│   └── repositories - all crud stuff.
├── models           - pydantic models for this application.
│   ├── domain       - main models that are used almost everywhere.
│   └── schemas      - schemas for using in web routes.
├── resources        - strings that are used in web responses.
├── services         - logic that is not just crud related.
└── main.py          - FastAPI application creation and configuration.
```

## pre-commit

Content: .pre-commit-config.yaml

```
pre-commit run --all-files
pre-commit install
```

## TODO

- [ ] Add different responses for exceptions (resolver.NoAnswer, resolver.NXDOMAIN)
- [ ] Add other types of records
- [ ] Add integration tests

## Coverage

coverage run --source='.' -m pytest
