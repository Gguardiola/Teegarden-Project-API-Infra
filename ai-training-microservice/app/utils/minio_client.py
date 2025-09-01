from minio import Minio
import os

minio_client = Minio(
    "minio-bucket:9000",
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

BUCKET_NAME = "models"