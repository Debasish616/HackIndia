from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from .routers import auth
from .database import engine
from .models import Base

app = FastAPI(
    title="UniPe Auth Server",
    description="This is the authentication server for UniPe. This will be used in all the UniPe services to authenticate the users.",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def read_root():
    return {"message": "Welcome to the UniPe Auth Server"}
