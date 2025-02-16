# interview-tokio-marine

TMHCC Insurance Underwriting Project - Senior Software Developer Interview Exercise.

```bash
$ make help
interview-tokio-marine v0.1.0
TMHCC Insurance Underwriting Project - Senior Software Developer Interview Exercise.

Usage: make <command>

Commands:
  help       List available command.
  docs       Run documentation.
  lint       Run static code quality checks.
  tests      Run tests.
  run        Run application.
  config     Create environment configuration files.
  init       Download project dependencies.
  clean      Clean project files.

```

## Usage

Please see `docs/src/openapi.json` for the API documentation.

### Prerequities

I use `GNU Make` and `Poetry` to simplify the usage for this project. You can run this project without them but they speed things up considerably.

Look in the `Makefile` for the individual commands you'd need to run the project.

### Running locally

1. Run `make config` to create the `config/.env.local`
3. Run `make init` to download the package dependencies
4. Run `make run` to run the API locally
5. Go the browser to use the API e.g. `http://localhost:3000/api/v1/policies`

## Development

I use `GNU Make` and `Poetry` to simplify the usage for this project. You can run this project without them but they speed things up considerably.

Look in the `Makefile` for the individual commands you'd need to run the project.

I've used `pyenv` to automatically set the python version to 3.12. Please ensure your python version matches if you're not using `pyenv`

### Running tests

1. Run `make config` to create the `config/.env.local`
3. Run `make init` to download the package dependencies
4. Run `make tests` to run the tests using `pytest`