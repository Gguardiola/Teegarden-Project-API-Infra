from fastapi import APIRouter, status, Header, HTTPException
from fastapi.responses import JSONResponse
from dto.combat_log_dto import CombatLogDTO
import service.combat_log_service as CombatLogService
from utils.auth import verify_token

router = APIRouter()
print("[CombatLogRouter] Initializing combat log router")

@router.post("/combatlog")
async def post_combat_log(combat_log: CombatLogDTO, authorization: str = Header(...)):
    print("[POST /combatlog] Received combat log")
    token = authorization.split(" ")[1]
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    inserted_id = await CombatLogService.save_combat_log(combat_log)
    return JSONResponse(
        status_code=201,
        content={"status": "processed", "id": str(inserted_id)}
    )