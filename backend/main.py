from fastapi import FastAPI
from db.database import engine
from db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running"}