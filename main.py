import uvicorn

from src.analysis import Analysis
from src.crawler import Crawler
from src.kernel import Config
from src.web_api import app

if __name__ == "__main__":
    config = Config()

    background_tasks = [
         Analysis,
         Crawler
    ]

    # Instance subprocesses
    subprocesses = map(lambda x: x(config), background_tasks)

    # Start subprocesses
    for do in subprocesses:
        temp=[]
        do.start()

    # Blcok main process
    uvicorn.run(app, host="0.0.0.0", port=8000)

    # Stop subprocesses
    for do in subprocesses:
        do.terminate()
