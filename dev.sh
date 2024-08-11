#!/bin/bash

# Determine the environment, or default to local
export ENV="${1:-local}"
if [ "$ENV" != "local" ] && [ "$ENV" != "prod" ] && [ "$ENV" != "qa" ]; then
    echo "Invalid argument. It must be one of 'local', 'prod', or 'qa'."
    exit 1
fi

# Inject secrets
op inject -i ./.env.tpl -o ./.env

# Build the image with secrets mounted
docker build -t fastapi-scaffolding-image . --target dev

# # Delete injected secrets 
# rm .env

# Run the image 
# - Run in an integrated terminal 
# - Remove image after running 
# - Name of the new container 
# - Mount all local files to a shared volume in \code
# - Expose ports for running and debugging 
# - Pass local secrets
# - Image to run 
docker run -it \
  --rm \
  --name fastapi-scaffolding-image-container \
  -v $(pwd):/code \
  -p 8080:8080 -p 5678:5678 \
  -e ENVIRONMENT=$ENV \
  --env-file=.env \
  fastapi-scaffolding-image    
