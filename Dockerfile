# base image
FROM python:3.8-slim

# set straight output into stdout
ENV PYTHONUNBUFFERED 1
# preventing the creation of *.pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# system dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# application dependencies
COPY requirements /tmp/requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -U app_user \
    && install -d -m 0755 -o app_user -g app_user /app/static

# files and permissions setup
RUN chown -R app_user:app_user /app
WORKDIR /app
USER app_user:app_user
COPY --chown=app_user:app_user . .
RUN chmod +x docker/*.sh

ENTRYPOINT [ "docker/entrypoint.sh" ]
