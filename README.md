# voikko

Dockerized Voikko library


## Publish image

Build docker image
- ./docker-build.sh

Tag docker image
- docker tag image username/repository:tag
- e.g. docker tag voikko ossidocker/voikko

Push image
- docker push username/repository:tag
- e.g. docker push ossidocker/voikko:latest


## Usage

Start container
- docker run -p 8000:8000 username/repository:tag
- e.g. docker run -p 8000:8000 ossidocker/voikko:latest

or

- docker-compose up

Shutdown container
- docker-compose down


## Testing

Start containers and run unit tests:
- python3 ./testing/run_tests.py



