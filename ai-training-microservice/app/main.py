from fastapi import FastAPI
from router import combat_log_router
from router import model_router
from router import auth_router
import os
print("[Main] Starting AI Training Microservice - version", os.environ.get("VERSION", "1.0.0"))

app = FastAPI()
app.include_router(model_router.router)
app.include_router(combat_log_router.router)
app.include_router(auth_router.router)

@app.get("/")
async def root():
    print("[GET /] Keep alive request received")
    return {"keep_alive": "awake"}

