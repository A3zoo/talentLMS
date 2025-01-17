from fastapi import FastAPI
from env import env
from app_environment import AppEnvironment
from fastapi.middleware.cors import CORSMiddleware
from controllers import (
    course_controller,
    login_controller
)

app = FastAPI(debug=env.DEBUG)

if AppEnvironment.is_local_env(env.APP_ENV):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(login_controller.router)
app.include_router(course_controller.router, prefix="/api")
