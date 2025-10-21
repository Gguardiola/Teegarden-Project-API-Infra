from pydantic import BaseModel

class RLState(BaseModel):
    actor: str
    actorHP: float
    actorEnergy: float
    actorShield: int
    opponent: str
    opponentHP: float
    opponentEnergy: float
    opponentShield: int

class RLExperience(BaseModel):
    state: RLState
    action: str
    reward: float
    next_state: RLState