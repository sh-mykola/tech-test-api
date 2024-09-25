#!/bin/bash

set -o errexit -o nounset -o pipefail

DO_FILE=$(python3 -c "import os, sys; print(os.path.abspath(sys.argv[1]))" "${BASH_SOURCE[0]}")
ROOT_FOLDER=$(dirname "$DO_FILE")
PYTHON_VERSION="3.12.0"
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8025}

function help() {
    echo "Tech | Python $PYTHON_VERSION"
    echo ""
    echo "Usage: $0 [command_name] [optional_argument]"
    echo ""
    echo "Available commands:"
    echo " $0 expose_port       - Expose port '${PORT}' via ngrok."
    echo " $0 docker_build      - Run docker-compose build."
    echo " $0 docker_up         - Run docker-compose up."
    echo " $0 format            - Run formatting."
    echo " $0 help              - Display general help and usage information."
    echo ""
}

function expose_port() {
    echo "Exposing port via ngrok..."
    cd "$ROOT_FOLDER"
    ngrok http "$HOST":"$PORT"
}

function docker_build() {
    echo "Running docker compose build..."
    cd "$ROOT_FOLDER"
    docker-compose build
}

function docker_up() {
    echo "Running docker compose up..."
    cd "$ROOT_FOLDER"

    if ! docker network ls | grep -q "tech_proxy_net"; then
      docker network create "tech_proxy_net"
    fi

    docker-compose up -d
}

function format() {
    echo "Running formatting..."
    cd "$ROOT_FOLDER"
    autoflake --remove-all-unused-imports --ignore-init-module-imports --recursive --in-place app/
    isort --settings-path project.toml app/
    black --config project.toml app/
}


# Main script
if [[ $# -eq 0 ]]; then
    help
    exit 1
fi

# Check if the function with the given name exists
if declare -f "$1" > /dev/null; then
    "$@"
else
    echo "Function '$1' not found. Available functions: './do help'"
    exit 1
fi
