import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router


# Resolve the directory where this file lives so paths are relative to the app package.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize the FastAPI application and wire up the trip-planning API router.
app = FastAPI()
app.include_router(router)

# Serve static assets (CSS, images, etc.) from app/static at the /static URL path.
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Allow cross-origin requests from any origin so the frontend can call the API without restrictions.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Jinja2 to look for HTML templates inside app/templates.
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/")
def home(request: Request):
    """Render the landing page with the trip planning form."""
    return templates.TemplateResponse(request, "index.html")
