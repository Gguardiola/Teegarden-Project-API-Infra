import re
from datetime import datetime
from utils.minio_client import minio_client, BUCKET_NAME

async def get_model_path(version: str) -> str:
    return f"models/{version}/model.bin"

async def get_latest_model_key() -> str:
    pattern = re.compile(r"intellicombat_model_ready_(\d{8}_\d{6})\.onnx")
    latest_obj = None
    latest_dt = None

    for obj in minio_client.list_objects(BUCKET_NAME, recursive=True):
        match = pattern.match(obj.object_name)
        if match:
            ts = match.group(1)
            dt = datetime.strptime(ts, "%Y%m%d_%H%M%S")
            if not latest_dt or dt > latest_dt:
                latest_dt = dt
                latest_obj = obj.object_name

    if not latest_obj:
        raise FileNotFoundError("No ONNX models found.")

    return latest_obj

async def model_exists(version: str) -> bool:
    expected_name = f"intellicombat_model_ready_{version}.onnx"
    found = minio_client.stat_object(BUCKET_NAME, expected_name)
    return found is not None