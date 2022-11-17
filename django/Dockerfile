FROM mateusoliveira43/poetry:1.2.2-python3.10.8-slim-bullseye
ENV PYTHONUNBUFFERED 1
WORKDIR /Django_app
ADD . /Django_app
EXPOSE 8000
EXPOSE 5678
COPY ./pyproject.toml /Django_app/pyproject.toml
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi --no-root
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
#    chown -R appuser /Django_app
#USER appuser
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'vscode-django-docker'. Please enter the Python path to wsgi file.
#CMD ["poetry", "run", "gunicorn", "--bind", ":8000", "--workers", "1", "Project_Django_Boilerplate_GAP.wsgi"]
CMD ["sh", "entrypoint.sh"]