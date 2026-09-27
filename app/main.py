from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine
from app.routes.web import router as web_router
from app.routes.auth import router as auth_router
from app.routes.expenses import router as expenses_router
from app.routes.planners import router as planners_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pocket Smart AI")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(web_router)
app.include_router(auth_router)
app.include_router(expenses_router)
app.include_router(planners_router)