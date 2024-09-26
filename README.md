# Tech Application

## Overview

The Tech Application is a Python-based backend service that interacts with a PostgreSQL database and an external Breweries API. It is containerized using Docker and orchestrated with Docker Compose.

## Architecture

The application consists of the following components:

1. **Backend Service**: A Python application that serves as the main backend service. It is built using a Docker image based on `python:3.12.0b2-slim-buster`. The backend service handles API requests, processes data, and interacts with the PostgreSQL database.

2. **PostgreSQL Database**: A PostgreSQL database container that stores the application's data. It is configured with the URI inside `.env` file.

3. **Networking**: Both the backend service and the PostgreSQL database are connected through a Docker network named `tech_proxy_net`.

## Configuration

The application uses environment variables defined in the `.env` file:

- `BREWERIES_API_URL`: URL for the Breweries API.
- `POSTGRES_URI`: URI for connecting to the PostgreSQL database.

## Running the Application

To run the application, use the `./do` script with the `docker_build` and `docker_run` commands. This script will build and start the Docker containers defined in the `docker-compose.yml` file.

### Steps to Run

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/sh-mykola/tech-test-api
    cd tech-test-api
    ```

2. **Create and Configure `.env` File**:
    Ensure the `.env` file is present in the root directory with the following content:
    ```dotenv
    BREWERIES_API_URL=https://api.openbrewerydb.org/v1
    POSTGRES_URI=postgresql://secret:secret@postgres:5432/db
    ```

3. **Build and Run the Containers**:
    ```sh
    ./do docker_build
    ./do docker_run
    ```

This command will:
- Build the Docker images for the backend service.
- Start the backend and PostgreSQL containers.
- Attach the containers to the `tech_proxy_net` network.

### Accessing the Application

- The backend service will be accessible at `http://127.0.0.1:8025/docs`.

## Rich Swagger UI

The application includes a rich Swagger UI where you can test the API endpoints. You can access it at `http://127.0.0.1:8025/docs`.

![Swagger UI Placeholder](docs/swagger-main.png)

## Logging

The application uses a custom logging configuration defined in `app/logger.py`. Logs are output to both the console and a file named `app.log`.

## Dependencies

The application dependencies are listed in the `requirements.txt` file and are installed during the Docker build process.

## License

This project is licensed under the MIT License.