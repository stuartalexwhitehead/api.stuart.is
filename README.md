[![Build Status](https://circleci.com/gh/stuartalexwhitehead/api.stuart.is.svg?style=shield&circle-token=fc1c2f84c4b1c8190a6043303a149c5e8abd297b)](https://travis-ci.org/stuartalexwhitehead/api.stuart.is)
[![Coverage Status](https://coveralls.io/repos/github/stuartalexwhitehead/api.stuart.is/badge.svg)](https://coveralls.io/github/stuartalexwhitehead/api.stuart.is)

# api.stuart.is
Experimental back-end service for https://stuart.is

## Setup
The only prerequisite is [`Docker`](https://www.docker.com/)

1. Clone the repository with `git clone git@github.com:stuartalexwhitehead/api.stuart.is.git api.stuart.is`
2. Enable git hooks with `cd api.stuart.is && ln -s bin/githooks/* .git/hooks`
3. Build the Docker image with `docker build -t api.stuart.is .`

## Entrypoint Commands
The Docker entrypoint expects these commands. Any commands which rely on linked images should be run via `docker-compose`.

| Command | Description |
| --- | --- |
| `start` | Start app |
| `test` | Run Django unit tests, with coverage reporting |
| `lint [file1] [file2] ...` | Run linting. By Default, all project files are linted. |

## PyCharm Configuration
We can confidently use a Docker image as the remote Python interpreter in PyCharm 2017. These instructions are aimed at Docker for Mac.

1. PyCharm -> Preferences
2. Project -> Project Interpreter
3. Little cog icon -> Add Remote
4. Choose appropriate Docker image settings
