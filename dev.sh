op inject -i ./.env.tpl -o ./.env
docker build -t fastapi-scaffolding-image . --target dev_app --secret id=ENV_SECRETS,src=.env
rm .env
docker run -it --rm --name fastapi-scaffolding-image-container -v $(pwd):/code -p 8080:8080 -p 5678:5678 fastapi-scaffolding-image 

