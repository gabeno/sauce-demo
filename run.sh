#!/bin/bash
set -e

echo -e "\n[Saucy Pans]: Setting up test environment\n"
docker-compose down
docker-compose up --build -d
# wait for nodes to be up
sleep 5

echo -e "\n[Saucy Pans]: Running tests for Edge browser\n"
docker-compose run sandbox pytest --driver=edge tests

echo -e "\n[Saucy Pans]: Running tests for Firefox browser\n"
docker-compose run sandbox pytest --driver=firefox tests

echo -e "\n[Saucy Pans]: Running tests for Chrome browser\n"
docker-compose run sandbox pytest --driver=chrome tests

echo -e "\n[Saucy Pans]: Cleaning up\n"
docker-compose down

echo -e "\n[Saucy Pans]: Done!"
