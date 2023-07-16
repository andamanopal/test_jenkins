FROM python:3.11.3-slim-buster


RUN apt-get update
RUN apt-get install libgomp1
RUN pip install "poetry==1.4.2"

WORKDIR /dashboard

COPY . .

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

# RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

#RUN pip3 install -v https://github.com/pallets/werkzeug/archive/refs/tags/2.0.1.tar.gz

# CMD ["pwd"]