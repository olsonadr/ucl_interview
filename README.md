# ucl_interview

## Project Structure

- **`src/`**: the source code for the individual assignments.
    - **`src/test/`**: the test cases for the assignments.

## Requirements

To run the tests for these assignments, you must setup one of the following:

- **Docker**: To build and run the containerized application.
- **Python and pytest**: To run tests locally without using Docker.

Ensure you have these tools installed and properly configured on your system.

## Docker Usage

### With compose:

- Build:
    ```shell
    docker compose build
    ```
- Run image:
    ```shell
    docker compose run --rm -it test
    ```

### Without compose:

- Build:
    ```shell
    docker build -t olsonadr/ucl_interview .
    ```
- Run image:
    ```shell
    docker run --name ucl_interview --rm -it olsonadr/ucl_interview
    ```

### Run existing image with src/test on your filesystem:

From the project root directory:
```shell
docker run --name ucl_interview --rm -v "$(pwd)/src:/app/src" -it olsonadr/ucl_interview
```
