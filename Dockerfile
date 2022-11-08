FROM mateusoliveira43/poetry:1.2.2-python3.10.8-slim-bullseye
ENV PYTHONUNBUFFERED 1
WORKDIR /Django_app
ADD . /Django_app
EXPOSE 8000
COPY ./pyproject.toml /Django_app/pyproject.toml
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi --no-root
CMD ["poetry", "run", "gunicorn", "--bind", ":8000", "--workers", "1", "Project_Django_Boilerplate_GAP.wsgi"]
