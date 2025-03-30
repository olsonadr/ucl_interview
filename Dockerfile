# syntax=docker/dockerfile:1.0-experimental

# Python version to install by default with pyenv
ARG PYTHON_VERSION=3.9
# Pipenv version matching the above version
ARG PIPENV_TAG=3.9-2023.07.3

################################################################################
# Pipenv installation
#  - Source: https://pipenv.pypa.io/en/latest/docker.html
################################################################################
FROM docker.io/oz123/pipenv:${PIPENV_TAG} AS builder

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD Pipfile /app/

WORKDIR /app
RUN pipenv lock -d
RUN pipenv sync -d

################################################################################
# Python dependencies
################################################################################
FROM docker.io/python:${PYTHON_VERSION} AS python_deps

WORKDIR /app
RUN mkdir -v /app/.venv

COPY --from=builder /app/.venv/ /app/.venv/

################################################################################
# Run app (run pytest tests)
################################################################################
FROM python_deps as run_app

WORKDIR /app
ADD src test /app/

CMD ["./.venv/bin/python", "-m", "pytest"]
