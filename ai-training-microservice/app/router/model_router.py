from fastapi import APIRouter, HTTPException, status, Header
from fastapi.responses import JSONResponse
import service.model_service as ModelService
from utils.auth import verify_token
from utils.minio_client import minio_client, BUCKET_NAME


router = APIRouter()
print("[ModelRouter] Initializing model router")

@router.get("/model")
async def get_model(version: str, authorization: str = Header(...)):
    print(f"[GET /model/] Requesting model version: {version}")

    token = authorization.split(" ")[1]
    user = await verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    try:
        if version == "latest":
            model_key = await ModelService.get_latest_model_key()
        else:
            expected_name = f"intellicombat_model_ready_{version}.onnx"
            try:
                minio_client.stat_object(BUCKET_NAME, expected_name)
            except:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Model version {version} does not exist"
                )
            model_key = expected_name

        url = minio_client.presigned_get_object(BUCKET_NAME, model_key)
        url = url.replace("http://minio-bucket:9000", "http://localhost")
        return JSONResponse(content={"download_url": url})

    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))