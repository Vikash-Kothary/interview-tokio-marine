#!/usr/bin/env make

INTERVIEW_TOKIO_MARINE_ID ?= 0
INTERVIEW_TOKIO_MARINE_NAME ?= interview-tokio-marine
INTERVIEW_TOKIO_MARINE_VERSION ?= v0.1.0
INTERVIEW_TOKIO_MARINE_DESCRIPTION ?= TMHCC Insurance Underwriting Project - Senior Software Developer Interview Exercise.

ENV ?= local
-include config/.env.${ENV}
-include config/secrets/.env.*.${ENV}
export

.DEFAULT_GOAL := help
.PHONY: help #: List available command.
help:
	@${AWK} 'BEGIN {FS = " ?#?: "; print "$(INTERVIEW_TOKIO_MARINE_NAME) $(INTERVIEW_TOKIO_MARINE_VERSION)\n$(INTERVIEW_TOKIO_MARINE_DESCRIPTION)\n\nUsage: make \033[36m<command>\033[0m\n\nCommands:"} /^.PHONY: ?[a-zA-Z_-]/ { printf "  \033[36m%-10s\033[0m %s\n", $$2, $$3 }' $(MAKEFILE_LIST)

.PHONY: docs #: Run documentation.
docs:
	@${MKDOCS} ${MKDOCS_CMD} -f docs/mkdocs.yml ${MKDOCS_OPTS}

.PHONY: lint #: Run static code analysis.
lint:
	@${BLACK} .

.PHONY: tests #: Run tests.
tests:
	@${PYTEST} --doctest-modules tests/

.PHONY: run #: Run Python app.
run: 
	@${UVICORN} ${UVICORN_OPTS} ${UVICORN_ARGS}

# Run scripts using make
%:
	@if [[ -f "scripts/${*}.sh" ]]; then \
	${BASH} "scripts/${*}.sh" ${LOGGER}; fi

.PHONY: init #: Download project dependencies.
init:
	@${POETRY} install

.PHONY: config #: Create environment-specific config files.
config: config/.env.${ENV}
config/.env.%:
	@cp -n config/.env.example config/.env.${ENV}

.PHONY: release 
release:
	@false

.PHONY: build #: Build backend app.
build: 
	@${POETRY} build

.PHONY: publish
publish:
	@${POETRY} publish

.PHONY: package
package:
	@false

.PHONY: deploy
deploy:
	@false

.PHONY: open
open:
	@${OPEN} ${FLASK_URL}

.PHONY: clean #: Clean project build files.
clean:
	@[[ ! -d .venv ]] || rm -r .venv
	@[[ ! -d .pytest_cache ]] || rm -r .pytest_cache
	@find . -name *.pyc -not -path *.venv* -delete
	@find . -name __pycache__ -not -path *.venv* -delete
	@find . -name *.egg-info -not -path *.venv* -print0 | xargs -0 rm -r