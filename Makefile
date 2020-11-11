ENV = env
PYBIN = $(ENV)/scripts
PYTHON = $(PYBIN)/python
PIP = $(PYBIN)/pip
PYFLAKE8 = $(PYTHON) -m flake8
MKDIR = mkdir
PYTEST = $(PYTHON) -m pytest
TESTDIR = tests
COVERAGE = $(PYTHON) -m coverage

.PHONY: help
help:
	@echo "make environ          # create virtual env and setup dependencies"
	@echo "make run_dev          # run REST API server"
	@echo "make lint             # check linting"
	@echo "make flake8           # alias for `make lint`"
	@echo "make tests            # runs tests"
	@echo "make coverage         # executes tests with coverage calculation"
	@echo "make help             # show this help"

.PHONY: run_dev
run_dev:
	$(PYTHON) -m app.app
	
.PHONY: environ
environ: clean requirements.txt requirements-dev.txt
	virtualenv $(ENV)
	$(PIP) install -r requirements-dev.txt
	$(MKDIR) log
	$(MKDIR) tmp
	@echo "initialization complete"

.PHONY: lint
lint:
	$(PYFLAKE8)
	
.PHONY: flake8
flake8:
	$(PYFLAKE8)

.PHONY: clean
clean:
	if exist $(ENV) rd $(ENV) /q /s
	if exist .coverage del .coverage
	if exist __pycache__ rd __pycache__ /q /s		
	if exist log rd log /q /s	
	if exist tmp rd tmp /q /s
	echo stub > delete_me.pyc
	del /S *.pyc

.PHONY: tests
tests:
	$(PYTEST) $(TESTDIR) -vvv

.PHONY: coverage
coverage:
	$(PYTEST) $(TESTDIR) -vvv --cov=$(MODULE_NAME)
	$(COVERAGE) html
