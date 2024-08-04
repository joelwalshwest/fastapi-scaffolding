docker build -t joelwalshwest/fastapi-scaffolding:prod-latest . --target prod_app --platform=linux/amd64
docker push joelwalshwest/fastapi-scaffolding:prod-latest
gcloud run deploy fastapi-scaffolding --image joelwalshwest/fastapi-scaffolding:prod-latest  --platform managed  --allow-unauthenticated --project fastapi-scaffolding
