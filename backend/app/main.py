from fastapi import FastAPI
from app import models, database
from app.routes import users


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="restaurant scheduling app")

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "backend api running"}
