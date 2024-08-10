# Dev image with a full development environment 

FROM joelwalshwest/my-development-environment AS dev

RUN apk add --no-cache python3 py3-pip

WORKDIR /code
COPY ./requirements.txt ./
RUN python -m venv /my-venv
RUN /my-venv/bin/pip install --no-cache-dir -r requirements.txt
ENV PATH="/my-venv/bin:$PATH"

COPY . . 

EXPOSE 8080

WORKDIR /root
ARG ENVIRONMENT=0
RUN --mount=type=secret,id=ENV_SECRETS  \
    cp -r /run/secrets .
WORKDIR /code

# Slim image with required dependencies only

FROM python:3.11-slim AS slim

WORKDIR /code
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 8080

WORKDIR /root
ARG ENVIRONMENT=0
RUN --mount=type=secret,id=ENV_SECRETS  \
    cp -r /run/secrets .
WORKDIR /code

CMD ["uvicorn", "src.main:app", "--timeout-keep-alive", "0", "--host", "0.0.0.0", "--port", "8080"]
