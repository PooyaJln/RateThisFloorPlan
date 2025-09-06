import os
from datetime import datetime, timedelta, timezone
from typing import Annotated
from uuid import UUID, uuid4

import dotenv
import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from passlib.context import CryptContext

dotenv.load_dotenv()
ACESS_TOKEN_SECRET = os.getenv("ACESS_TOKEN_SECRET")
bcrypt_context = CryptContext(schemes=["bcrypt"])


def verify_password(plain_password: str, hashed_password: str) -> str:
    return bcrypt_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)


def create_access_token(email: str, user_id: UUID, expires_delta: timedelta) -> str:
    encode = {
        "sub": email,
        "id": str(user_id),
        "exp": datetime.now(timezone.utc) + expires_delta,
    }

    return jwt.encode(encode, ACESS_TOKEN_SECRET, algorithm="SH256")
