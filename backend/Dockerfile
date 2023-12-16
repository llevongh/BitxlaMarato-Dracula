FROM python:3.9.12-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    COLUMNS=200 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    MXNET_SUBGRAPH_VERBOSE=0

WORKDIR /src

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libgomp1  git

RUN apt-get install build-essential -y


COPY ./src/requirements.txt ./requirements.txt


RUN pip install --upgrade pip \
    && pip install \
    --no-cache-dir -Ur /src/requirements.txt


COPY ./src /src
CMD ["/src/entrypoint.sh"]
