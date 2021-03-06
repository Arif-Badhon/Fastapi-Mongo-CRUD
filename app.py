from fastapi import FastAPI
from routes.user import user

description = "This is a practice demo app to undertand CRUD application better for the Data Terminal"

app = FastAPI(
    title = "Demo Data Terminal",
    version= "1.0.0.0",
    description=description
)

app.include_router(user)

@app.get("/")
def root():
    return {"message": "Demo Bangladeshis First Data Terminal"}