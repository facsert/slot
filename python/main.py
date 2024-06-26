"""
description: fastapi 
"""
from contextlib import asynccontextmanager

import uvicorn
from loguru import logger
from fastapi import FastAPI

from lib.logger import logger_setting
from lib.database import Database
from lib.middleware import add_middlewares
from utils.router import add_routers

HOST: str = "localhost"
PORT: int = 8010

@asynccontextmanager
async def lifespan(router: FastAPI):
    """ 应用开启和结束操作 """
    logger.info("launch server")
    logger_setting()
    Database.init()
    add_routers(router)
    yield
    Database.close()
    logger.info("close server")

app = FastAPI(
    title="FastAPI",
    description=f"{HOST}:{PORT} api",
    version="0.0.1",
    lifespan=lifespan
)

add_middlewares(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
