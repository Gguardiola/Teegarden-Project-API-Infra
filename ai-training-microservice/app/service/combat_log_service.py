# services/combat_log_service.py
from dto.combat_log_dto import CombatLogDTO
from dto.combat_log_rl_dto import RLExperience, RLState
import repository.combat_log_repository as CombatLogRepository
import repository.combat_log_rl_repository as RLLogRepository
from intellicombat_training_logs_manager.convert_log_to_rl_format import convert_log_to_rl_format


async def save_combat_log(dto: CombatLogDTO) -> str:
    #inserted_id = await CombatLogRepository.insert(dto)

    rl_raw_dataset = convert_log_to_rl_format(
        [t.dict() for t in dto.turns],
        dto.winner
    )

    rl_dataset = [
        RLExperience(
            state=RLState(**exp["state"]),
            action=exp["action"],
            reward=exp["reward"],
            next_state=RLState(**exp["next_state"])
        )
        for exp in rl_raw_dataset
    ]

    inserted_id = await RLLogRepository.insert_many(rl_dataset)

    return str(inserted_id)


# from dto.combat_log_dto import CombatLogDTO
# from dto.combat_log_dto import CombatLogDTO, Ability, Turn
# import repository.combat_log_repository as CombatLogRepository

# async def save_combat_log(dto: CombatLogDTO) -> str:
#     inserted_id = await CombatLogRepository.insert(dto)
#     return inserted_id

