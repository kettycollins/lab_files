from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
import structlog

app = FastAPI(title="Secure API")

logger = structlog.get_logger()


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    status: str


@app.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    logger.info("login_attempt", email=data.email)
    return LoginResponse(status="ok")
