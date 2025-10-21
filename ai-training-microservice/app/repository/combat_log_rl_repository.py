import database.combat_log_db as db
from dto.combat_log_rl_dto import RLExperience

async def insert_many(experiences: list[RLExperience]):
    docs = [exp.model_dump() for exp in experiences]
    result = await db.combat_logs.insert_many(docs)
    return result.inserted_ids