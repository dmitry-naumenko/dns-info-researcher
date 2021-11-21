![coverage](.github/assets/coverage.svg)
![Tests](https://github.com/dmitry-naumenko/dns-info-researcher/workflows/Deploy/badge.svg)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![wblack](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Dependabot Status](https://img.shields.io/badge/Dependabot-active-brightgreen.svg)](https://dependabot.com)

# DNS INFO RESEARCHER

Helper for getting DNS records. All methods are cached.

## Demo:

- OpenAPI
  https://dns.madn.top/docs
- Redoc
  https://dns.madn.top/redoc

## Table of Contents

- [Installation](#installation)
  - [Without docker](#without-docker)
  - [With docker](#with-docker)
  - [Kubernetes](#kubernetes)
- [Usage](#usage)
  - [URL](#url)
  - [Docs](#docs)
- [Project structure](#project-structure)
- [pre-commit](#pre-commit)
- [TODO](#todo)
- [CI](#ci)

## Installation

Create .env file in project root and set environment variables for application (example: .env.example).

#### Without docker

Install requirements:

- Local verision:
  `pip install -r requirements/local.txt`
- Production version:
  `pip install -r requirements/production.txt`

Run the web application:

`uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

#### With docker

You must have docker and docker-compose tools installed to work with material in this section.

- Local version:
  `docker-compose -f docker-compose-local.yml up -d --build`
- Production version:
  `docker-compose -f docker-compose-production.yml up -d --build`

#### Kubernetes

Use kubernetes.yaml and autoscale.yaml

## Usage

### URL

The application will be available on localhost in your browser.

### Docs

All routes are available on /docs or /redoc paths with Swagger or ReDoc.

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

## Project structure

Files related to application are in the app or tests directories. Application parts are:

```
app
├── api              - web related stuff.
│   └── endpoints    - web routes.
├── core             - application configuration, startup events, logging, caching.
├── models           - pydantic models for this application.
│   └── schemas      - schemas for using in web routes.
├── services         - business logic.
└── main.py          - FastAPI application creation and configuration.
tests                - tests
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

## CI

Look at directories: scripts, .github.
