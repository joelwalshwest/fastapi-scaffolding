docker build -t fastapi-scaffolding-image . --target dev_app    
docker run -it --rm --name fastapi-scaffolding-image-container -p 8080:8080 -p 5678:5678 -v $(pwd):/code fastapi-scaffolding-image 
