import database.combat_log_db as db
from dto.combat_log_dto import CombatLogDTO

async def insert(entity: CombatLogDTO):
    result = await db.combat_logs.insert_one(entity.model_dump())
    return result.inserted_id