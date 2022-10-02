FROM python:3.8

COPY app/ /api-tcc/app/

COPY poetry.lock pyproject.toml /api-tcc/

WORKDIR api-tcc

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
