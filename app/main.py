from fastapi import FastAPI
app = FastAPI(title="Apertur-API")

@app.get("/")
async def root():
    return {"message": "Welcome to Apertur API"}