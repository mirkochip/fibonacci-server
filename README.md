[![Code Coverage](coverage.svg)](coverage.svg)

# Fibonacci Server
A web server able to calculate, one at a time, the subsequent items in the Fibonacci sequence. 

This server implements a REST API interface and it is configured for listening to incoming HTTP requests made towards the port 8080. For every HTTP request made, it replies with a JSON, rendering the next Fibonacci expected value.

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

This will start the server, being ready to serve the incoming HTTP requests sent to `localhost:8080`.

### Developers 
For development purposes it is possible to make the DB migration file, applying the required migrations and starting the server running the following commands:

```
python manage.py makemigrations fibonacci
python manage.py migrate
python manage.py runserver 8080
```

The provided `Makefile` offers some "candies" for developers, including useful targets for speeding up the development.

`make run`:  Condensate the execution of the commands listed above into just one command.

By default the log level of the application is set to `DEBUG` which, for every request, prints out in the server console the partial Fibonacci sequence. The log level, handler and formatter could be configured into the `LOGGING` section defined in `src/settings.py`.  

## API Endpoints

`GET /`: gets the next Fibonacci sub-sequence item.

`DELETE /`: reset the whole sequence, allows playing again from scratch.

## Unit Tests (and Code Coverage)
The unit tests have been provided into `src/tests` directory and aim to cover as much coded business logic as possible.

It is possible to run the battery of unit tests and generating the coverage report using the following command:

`coverage run --source="." manage.py test --verbosity 2`

The provided `Makefile` contains a useful target for testing:

`make test`: to run the unit tests, generating the coverage report and refreshing the coverage badge. 

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
The `fibonacci-server` application comes along with a `Dockerfile` which allows to ship it as a Docker image based on a `python:3.8-slim` image.

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
1. The principal `fibonacci-server` endpoint was configured, as requested, pointing to `/`. In order to have better control over API versioning, it would be better to point it to `/api/v1/fibonacci` instead. The Python modules in the project are already structured to support it.  
2. For sake of simplicity, no standalone webserver (e.g. `gunicorn`) was installed/configured. For ready-to-production applications, this is a must-have.
3. A SQL database (SQLite) was used, in order to handle the persistence of the partial Fibonacci sequence over the application reboots. Different solutions (e.g. Django memcached, PostgresSQL, NoSQL databases, etc.) might be used, depending on the infrastructure/users needs.