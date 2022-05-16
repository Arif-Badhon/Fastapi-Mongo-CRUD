from fastapi import FastAPI
from routes.user import user

description = "This is a practice demo app to undertand CRUD application better"

app = FastAPI(
    title = "Simple CRUD Application",
    version= "1.0.0.0",
    description=description
)

app.include_router(user)

@app.get("/")
def root():
    return {"message": "Simple CRUD Application"}