# This file is licensed under the Affero General Public License version 3 or
# later. See the LICENSE file.

uid=$(shell id -u)
gid=$(shell id -g)
project_directory=$(CURDIR)

# Dev env management
dev-setup:
	poetry install
	poetry run python3 manage.py migrate

