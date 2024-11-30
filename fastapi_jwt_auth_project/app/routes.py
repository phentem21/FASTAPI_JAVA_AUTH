from fastapi import APIRouter, Depends, HTTPException, status
from app.models import User, Token, TokenData
from app.utils import create_access_token, decode_token, hash_password, verify_password
from app.database import user_collection
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_user(email: str):
    return user_collection.find_one({"email": email})

def authenticate_user(email: str, password: str):
    user = get_user(email)
    if user and verify_password(password, user["password"]):
        return user
    return False

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"email": payload.get("sub")}
