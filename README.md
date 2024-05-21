# Selenium Grid in docker

This will spin up a selenium grid with http basic auth using docker

## Running

1. Run the docker compose

    ```bash
    docker compose up -d --build
    ```

2. Install the python requirements

    - Using poetry: `poetry install`
    - Using pip: `pip install selenium`

3. Running the example: `python example.py`
