from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import get_settings
from .database import init_db

from .routes.auth import router as auth_router
from .routes.planners import router as planners_router
from .routes.web import router as web_router


settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):

    init_db()

    yield


app = FastAPI(
    title=settings.app_name,

    description=(
        "Budget-aware AI recommendation "
        "assistant for home, parties, "
        "and jewelry."
    ),

    version="1.0.0",

    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.mount(
    "/static",
    StaticFiles(
        directory="app/static"
    ),
    name="static",
)


app.include_router(
    web_router
)

app.include_router(
    auth_router
)

app.include_router(
    planners_router
)


@app.get(
    "/health",
    tags=["system"],
)
def health():

    return {
        "status": "ok",
        "app": settings.app_name,
        "ai_configured": bool(
            settings.gemini_api_key
        ),
        "model": settings.gemini_model,
    }


@app.get(
    "/startup",
    tags=["system"],
)
def startup():

    init_db()

    return {
        "status": "initialized",
        "database": "ready",
        "ai_configured": bool(
            settings.gemini_api_key
        ),
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )