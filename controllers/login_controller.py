from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter
from services.authen_service import create_token

router = APIRouter()

# Đăng nhập sẽ trả về token
@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return create_token(form_data.username, form_data.password)






