from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
import os 

print("[Auth] Loading secrets...")
SECRET_KEY = os.getenv("API_SECRET")
print("[Auth] Secrets loaded!")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

mocked_users = {
    "player1": {
        "username": "player1",
        "hashed_password": pwd_context.hash("password123")
    },
    "local_debug_player": {
        "username": "local_debug_player",
        "hashed_password": pwd_context.hash("password123")
    }
}


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = mocked_users.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    print(f"[Auth] User authenticated: {username}")
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(f"[Auth] Token created for user: {data.get('sub')}")
    return encoded_jwt

async def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        print(f"[Auth] Token verified for user: {username}")
        return username
    except JWTError:
        return None