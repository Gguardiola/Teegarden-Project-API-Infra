from minio import Minio

minio_client = Minio(
    "minio-bucket:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

BUCKET_NAME = "models"