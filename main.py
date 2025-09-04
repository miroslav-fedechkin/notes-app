from fastapi import FastAPI
from app.router import router as tasks_router


app = FastAPI()
app.include_router(tasks_router)


