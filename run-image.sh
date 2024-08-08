docker build -t fastapi-scaffolding-image . --target prod_app    
docker run --name fastapi-scaffolding-image-container --rm -it -p 80:80 -p 5678:5678 -v $(pwd):/code fastapi-scaffolding-image 
