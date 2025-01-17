import os

from dotenv import load_dotenv
from pydantic import BaseModel
from app_environment import AppEnvironment

app_env = os.getenv("APP_ENV")

if (app_env is None) or (app_env not in AppEnvironment.__members__):
    raise ValueError(f"APP_ENV not set, or invalid value. Valid values are: {', '.join(AppEnvironment.__members__)}")

app_env = AppEnvironment(app_env)

if app_env == AppEnvironment.test:
    load_dotenv(".env.test")
else:
    load_dotenv(".env")

class Env(BaseModel):
    TALENTLMS_API_KEY: str
    TALENTLMS_BASE_URL: str
    DEBUG: bool
    APP_ENV: AppEnvironment
    SECRET_KEY: str
    HOST: str
    PORT: int

env = Env.model_validate(os.environ)
