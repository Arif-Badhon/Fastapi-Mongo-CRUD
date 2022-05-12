from fastapi import FastAPI


description = "This is a practice demo app to undertand CRUD application better"

app = FastAPI(
    title = "Simple CRUD Application",
    version= "1.0.0.0",
    description=description
)


@app.get("/")
def root():
    return {"message": "Simple CRUD Application"}