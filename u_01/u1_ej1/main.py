from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola mundo"}

@app.get("/ping")
async def ping():
    return{"status": "ok", "ts": "2026-09-08"}