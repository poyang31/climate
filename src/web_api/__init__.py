from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from .routers import filter, rank, statistics

app = FastAPI()

current_path = Path(__file__).parent.resolve()

app.mount(
    path="/static",
    app=StaticFiles(directory=f"{current_path}/../../web/static"),
    name="static"
)

app.include_router(
    prefix="/filter",
    router=filter.router,
    tags=["filter"],
    responses={418: {"description": "I'm a teapot"}},
)

app.include_router(
    prefix="/rank",
    router=rank.router,
    tags=["rank"],
    responses={418: {"description": "I'm a teapot"}},
)

app.include_router(
    prefix="/statistics",
    router=statistics.router,
    tags=["statistics"],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def read_index():
    return FileResponse(f"{current_path}/../../web/index.html")
