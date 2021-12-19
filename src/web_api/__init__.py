from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

root_path = Path(__file__).parent.resolve()
app.mount(
    "/static",
    StaticFiles(directory=f"{root_path}/../../web/static"),
    name="static"
)


@app.get("/")
async def read_index():
    return FileResponse('web/index.html')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
