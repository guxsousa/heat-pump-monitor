# Python Project Template

This project is ...


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/guxsousa/xxxxxxxxx.git
    ```

2. Navigate to the project directory:
    ```sh
    cd xxxxxxxxx
    ```

3. Install Poetry if you haven't already:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

4. Initiate a new Python project:
    ```sh
    poetry init
    ```

4. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

5. Activate the virtual environment:
    ```sh
    poetry shell
    ```


## Usage

Provide examples of how to use the project:
```sh
cd module
python core.py --help
```


## Installation with Docker

Build Dockerfile
```sh
docker build -t cal .
```

Find image-id
```sh
docker images 
```

Run iterative session
```sh
docker run --rm -ti -p 8080:8080 <copied-image>
```

Verify active session
```sh
docker ps --all
```
