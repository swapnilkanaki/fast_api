from fastapi import FastAPI
from model import dataUse
from database import collecton_name
from schemas import dataUse_serializer,dataUses_serializer
app = FastAPI()


@app.get("/")
def get_data():
    # return {" data ": " this sample data"}
    return dataUses_serializer(collecton_name.find())

@app.post("/")
def add_data(data : dataUse):
    collecton_name.insert_one(dict(data))
    return {" msg ": " Data Added "}