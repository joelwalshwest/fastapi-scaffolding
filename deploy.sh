docker build -t joelwalshwest/fastapi-scaffolding . --target prod_app --platform=linux/amd64
docker push joelwalshwest/fastapi-scaffolding
gcloud run deploy fastapi-scaffolding --image joelwalshwest/fastapi-scaffolding  --platform managed  --allow-unauthenticated
