FROM postgres:15

RUN apt-get update && apt-get install -y postgresql-server-dev-15

RUN mkdir /sqlscripts

COPY --chown=postgres:postgres startup.sh /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres sql/create_tables.sql /sqlscripts/
COPY --chown=postgres:postgres sql/seed.sql /sqlscripts/
COPY --chown=postgres:postgres sql/create_users.sql /sqlscripts/