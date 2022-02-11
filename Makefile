#!/bin/bash
SYS_PYTHON=/usr/bin/python3.8
VENV_BIN:=venv/bin
DEV_PYTHON=$(VENV_BIN)/python3
PIP:=$(VENV_BIN)/pip3
COVERAGE:=$(VENV_BIN)/coverage
DEPS:=requirements.txt
PORT:=8080

venv:
	$(SYS_PYTHON) -m venv venv

setup:
	$(PIP) install --upgrade pip
	$(PIP) install -U pip -q
	$(PIP) install -r $(DEPS)

check:
	$(VENV_BIN)/isort src
	$(VENV_BIN)/flake8 src

test:
	$(COVERAGE) run --source="." manage.py test --verbosity 2
	$(COVERAGE) report -m
	rm -f coverage.svg
	$(VENV_BIN)/coverage-badge -o coverage.svg

run:
	$(DEV_PYTHON) manage.py runserver $(PORT)
