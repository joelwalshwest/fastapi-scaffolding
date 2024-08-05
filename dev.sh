docker build -t fastapi-scaffolding-image . --target dev_app    
docker run -it -p 80:80 -p 5678:5678 -v $(pwd):/code fastapi-scaffolding-image 
