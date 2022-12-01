FROM mateusoliveira43/poetry:1.2.2-python3.10.8-slim-bullseye
ENV PYTHONUNBUFFERED 1
#=====================TEST ENVs===================
ENV DJANGO_SETTINGS_MODULE Project_Django_Boilerplate_GAP.settings
ENV DJANGO_ADMIN_USER admin
ENV DJANGO_ADMIN_EMAIL admin@info.com
ENV DJANGO_ADMIN_PASS admin
ENV KEYCLOAK_CLIENT_ID DjangoApp
ENV KEYCLOAK_CLIENT_SECRET 4ph4iZ83f4YpBALCNFkndL9UbiPEVGcf
ENV SITE_BASE_URL http://host.docker.internal:8000/
ENV KEYCLOAK_URL http://host.docker.internal:8080/
ENV REALM_NAME default
ENV KEYCLOAK_ADMIN_CLIENT_ID admin-cli
ENV KEYCLOAK_ADMIN_USERNAME admin
ENV KEYCLOAK_ADMIN_PASSWORD admin
#=====================+++++++===================
WORKDIR /Django_app
ADD . /Django_app
EXPOSE 8000
EXPOSE 5678
COPY ./pyproject.toml /Django_app/pyproject.toml
RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi --no-root
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
#    chown -R appuser /Django_app
#USER appuser
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'vscode-django-docker'. Please enter the Python path to wsgi file.
#CMD ["poetry", "run", "gunicorn", "--bind", ":8000", "--workers", "1", "Project_Django_Boilerplate_GAP.wsgi"]
CMD ["sh", "entrypoint.sh"]