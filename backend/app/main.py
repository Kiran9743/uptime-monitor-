from fastapi import FastAPI, BackgroundTasks
from .monitor import start_monitoring, get_status

app = FastAPI(title="Uptime Monitor - Backend")

@app.on_event("startup")
async def startup_event():
    # start background monitoring tasks
    start_monitoring()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/status")
async def status():
    return get_status()
