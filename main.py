from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def jname():
    return {"name": "John Doe1"}