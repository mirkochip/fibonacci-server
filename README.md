[![Code Coverage](coverage.svg)](coverage.svg)

# Fibonacci Server
A web server able to calculate, one at a time, the subsequent items in the Fibonacci sequence. 

This server implements a REST API interface and it is configured for listening to incoming HTTP requests made towards the port 8080. For every HTTP request made, it replies with a JSON rendering the next Fibonacci expected value.

Here it is following an example of the first 7 sequential requests and the related expected responses:

```
mirkochip@venus:fibonacci-server$ curl -s localhost:8080 | python -m json.tool
{
    "value": 0
}
mirkochip@venus:fibonacci-server$ curl -s localhost:8080 | python -m json.tool
{
    "value": 1
}
mirkochip@venus:fibonacci-server$ curl -s localhost:8080 | python -m json.tool
{
    "value": 1
}
mirkochip@venus:fibonacci-server$ curl -s localhost:8080 | python -m json.tool
{
    "value": 2
}
mirkochip@venus:fibonacci-server$ curl -s localhost:8080 | python -m json.tool
{
    "value": 3
}
mirkochip@venus:fibonacci-server$ curl -s localhost:8080 | python -m json.tool
{
    "value": 5
}
mirkochip@venus:fibonacci-server$ curl -s localhost:8080 | python -m json.tool
{
    "value": 8
}
```


# Installation and usage

## Software requirements
The project has been developed using the following stack of core technologies:

- Python `3.8.10`
- Django `4.0.2`
- Django REST Framework `3.13.1`

and it has been packaged using Docker `20.10.12`.

## Setup of the local development environment
- Clone in the local file system the `fibonacci-server` repository and `cd fibonacci-server`. 
- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: ` source venv/bin/activate`
- Install the required dependencies: ` pip install -r requirements.txt`

The provided `Makefile` could facilitate the operations mentioned above, running the following targets:

`make venv`: create the `venv` Python virtual environment.

`make setup`: upgrade pip and install the required dependencies into `venv`.


## Usage

### End Users
The `fibonacci-server` is supposed to be released and then shipped as a Docker image ready to be consumed by the end-users. Provided that, the `fibonacci-server` image was already pulled from a Docker registry (e.g. JFrog, etc.), it will be possible to consume it running the following simple command:

`docker run {image_hash}`

This will start the server, ready to serve the incoming HTTP requests at `localhost:8080`.

### Developers 
For development purposes it is possible to make the DB migration file, applying the required migrations and starting the server running the following commands:

```
python manage.py makemigrations fibonacci
python manage.py migrate
python manage.py runserver 8080
```

The provided `Makefile` offers some "candies" for developers, including useful targets for speeding up the development.

`make run`:  Condensate the execution of the commands listed above into just one command.

It will also be possible:

## Unit Tests (and Code Coverage)
The unit tests have been provided into `src/tests` directory. They aim to cover as much application business logic as possible.

It is possible to run the battery of unit tests and generating the coverage report using the following command:

`coverage run --source="." manage.py test --verbosity 2`

The provided `Makefile` contains a useful target for testing:

`make test`: to run the unit tests, generate and print out in stdout the coverage report and refreshing the coverage badge. 

Here it is following an outcome of test run and coverage report:

```
test_delete (src.tests.api.v1.fibonacci.test_views.TestFibonacciView) ... ok
test_get (src.tests.api.v1.fibonacci.test_views.TestFibonacciView) ... ok
test_get_next_fibonacci_value_init (src.tests.api.v1.fibonacci.test_views_models.TestFibonacciViewsModels) ... ok
test_get_next_fibonacci_value_steps_back (src.tests.api.v1.fibonacci.test_views_models.TestFibonacciViewsModels) ... ok
test_set_fibonacci_series (src.tests.api.v1.fibonacci.test_views_models.TestFibonacciViewsModels) ... ok

Name                                   Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------
src/api/v1/fibonacci/models.py             3      0      2      0   100%
src/api/v1/fibonacci/serializers.py        3      0      2      0   100%
src/api/v1/fibonacci/views.py             16      0      2      0   100%
src/api/v1/fibonacci/views_models.py      16      0      6      0   100%
----------------------------------------------------------------------------------
TOTAL                                     38      0     12      0   100%
```

## Linting
Some clean code utilities, `flake8` and `isort`, have been provided aiming to ensure to deliver PEP8 compliant codebase. 

It is possible to run such utilities running the two following commands:

```
isort src
flake8 src
```

Or, just using the `check` target available in the `Makefile`:

`make check`

## Docker
The `fibonacci-server` application comes along with a `Dockerfile` which allows to ship it as a Docker image based on a `python:3.8-slim` Docker container.

In order to build a new Docker image, run the following command:

`docker build .`

## Contribute to the project
In order to contribute to `fibonacci-server` project, the following steps should be followed:
- branching out from `master` branch creating one of the following branch:
  - `feature/<ticket_id>_feature_task_title`
  - `bugfix/<ticket_id>_bugfix_task_title`
- commit and push changes in the feature/bugfix branch
- open a pull request from feature/bugfix branch towards `master` 
- once the change is merged into master, make a release creating a tag

## Notes
Server listening at / and not to api/v1/fibonacci..
No Webserver configured