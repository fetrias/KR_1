from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models import User

app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

my_user = User(
    name="Петушкова Дарья",
    id=1
)

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@app.get("/users")
async def get_user():
    return my_user