# This folder is intended to store serve account keys. 

These keys need to be downloaded manually and should never be stored in version control.

Using these files (by exporting the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to one of these files) allows the container to run as the associated Cloud Run service account that runs the container on GCP. 

The expected account keys for this project are:
- fastapi-scaffolding.json (for account: fastapi-scaffolding@fastapi-scaffolding.iam.gserviceaccount.com)
- qa-fastapi-scaffolding.json (for account: qa-fastapi-scaffolding@fastapi-scaffolding.iam.gserviceaccount.com)