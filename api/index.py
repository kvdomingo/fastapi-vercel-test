from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)


@app.get("/", response_class=PlainTextResponse)
async def index():
    return "ok"
