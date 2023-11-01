from fastapi import FastAPI

from tasks.main import process_data

app = FastAPI()


@app.post("/process/")
async def process_endpoint(data: str):
    process_data.send(data)
    return {"message": "Task received, processing data."}
