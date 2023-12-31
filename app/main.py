from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models 
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# print (settings.database_user)

# models.Base.metadata.create_all(bind=engine) #this was the command that told sqlalchemy to run its staments, now we have alembic

app = FastAPI()

# origins = ["https://www.google.com", "https://www.youtube.com"]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World message generated from main.py"} 

