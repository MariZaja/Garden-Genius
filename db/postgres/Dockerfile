FROM postgres:16-alpine

# Install Python3, pip, and venv in the container
RUN apk add --no-cache python3 py3-pip py3-virtualenv

# Create a virtual environment for Python packages
RUN python3 -m venv /venv

COPY init.sql /docker-entrypoint-initdb.d/
COPY init_db_data.py /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init_db_data.py
COPY requirements.txt /docker-entrypoint-initdb.d/
COPY data.json /docker-entrypoint-initdb.d/
RUN /venv/bin/pip install --no-cache-dir -r /docker-entrypoint-initdb.d/requirements.txt


EXPOSE 5432

CMD ["docker-entrypoint.sh", "postgres", "-c", "exec /docker-entrypoint-initdb.d/init.py"]

# not working
# not working usage of init script