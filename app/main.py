from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router


app = FastAPI()
app.include_router(router)  # Placeholder for actual router import
app.mount("/static", StaticFiles(directory="static"), name="static")  # Placeholder for static files setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Holiday Agent is running!"}
    