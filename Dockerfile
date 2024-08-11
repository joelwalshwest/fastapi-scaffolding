# Dev image with a full development environment 

FROM joelwalshwest/my-development-environment AS dev

RUN apk add --no-cache python3 py3-pip

WORKDIR /code
COPY ./requirements.txt ./
RUN python -m venv /my-venv
RUN /my-venv/bin/pip install --no-cache-dir -r requirements.txt
ENV PATH="/my-venv/bin:$PATH"

COPY . . 

# Slim image with required dependencies only

FROM python:3.11-slim AS slim

WORKDIR /code
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD ["uvicorn", "src.main:app", "--timeout-keep-alive", "0", "--host", "0.0.0.0", "--port", "8080"]