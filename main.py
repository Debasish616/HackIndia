# main.py

from fastapi import FastAPI
from app.routers import signup, login, phone_auth  # import the new router

app = FastAPI()

app.include_router(signup.router)
app.include_router(login.router)
app.include_router(phone_auth.router)  # include the new router

# other code...
