#!/bin/bash

# Determine the environment, must be prod 
export ENV="${1}"
if [ "$ENV" != "prod" ] && [ "$ENV" != "qa" ]; then
    echo "Invalid argument. It must be either 'prod' or 'qa'."
    exit 1
fi

if [ "$ENV" == "prod" ]; then
    docker build -t joelwalshwest/fastapi-scaffolding:prod-latest . --target slim --platform=linux/amd64  --no-cache
    docker push joelwalshwest/fastapi-scaffolding:prod-latest
    gcloud run deploy fastapi-scaffolding --image joelwalshwest/fastapi-scaffolding:prod-latest --platform managed  --allow-unauthenticated --project fastapi-scaffolding
elif [ "$ENV" == "qa" ]; then
    docker build -t joelwalshwest/fastapi-scaffolding:qa-latest . --target slim --platform=linux/amd64 --no-cache
    docker push joelwalshwest/fastapi-scaffolding:qa-latest
    gcloud run deploy qa-fastapi-scaffolding --image joelwalshwest/fastapi-scaffolding:qa-latest  --platform managed  --allow-unauthenticated --project fastapi-scaffolding
fi