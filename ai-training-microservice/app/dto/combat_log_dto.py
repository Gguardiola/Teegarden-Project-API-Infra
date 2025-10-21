from pydantic import BaseModel
from typing import List

class Ability(BaseModel):
    abilityName: str
    abilityDescription: str
    damage: float
    cost: float
    isHealAbility: bool
    healAmount: float
    isShieldIgnored: bool
    isPoisonLike: bool

class Turn(BaseModel):
    turnNumber: int
    actor: str
    abilityUsed: str
    healAmount: float
    abilityDamage: float
    abilityEnergyCost: float
    actorHP: float
    actorEnergy: float
    opponentHP: float
    opponentEnergy: float
    isShieldAction: bool
    isSkippedAction: bool
    isHealingAbility: bool
    wasEffective: bool

class CombatLogDTO(BaseModel):
    enemyInitialAbilities: List[Ability]
    discoveredPlayerAbilities: List[Ability]
    turns: List[Turn]
    winner: str
