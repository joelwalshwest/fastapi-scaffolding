# Dev Image

# Build with:
# docker build -t fastapi-scaffolding-image . --target dev_app

# Run with: 
# docker run -it -p 80:80 -p 5678:5678 -v $(pwd):/code fastapi-scaffolding-image

FROM joelwalshwest/my-development-environment AS dev_app

RUN apk add --no-cache python3 py3-pip

WORKDIR /code
COPY ./requirements.txt ./
RUN python -m venv /my-venv
RUN /my-venv/bin/pip install --no-cache-dir -r requirements.txt
ENV PATH="/my-venv/bin:$PATH"

COPY ./src ./src

COPY run.sh .
RUN chmod 755 run.sh


# Prod Image

# Build with:
# docker build -t fastapi-scaffolding-image . --target prod_app

# Run with: 
# docker run -it -p 80:80 fastapi-scaffolding-image

FROM python:3.11-slim AS prod_app

WORKDIR /code
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--timeout-keep-alive", "0", "--host", "0.0.0.0", "--port", "8080"]
