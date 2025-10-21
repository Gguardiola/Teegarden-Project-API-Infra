import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongodb:27017")
db = client["intellicombat"]
combat_logs = db["combat_logs"]