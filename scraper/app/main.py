import logging

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from app.routers import scrape, scrapling, trafilatura

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

app = FastAPI(
    title="Scraper API",
    description="Trafilatura + Scrapling 통합 스크래핑 서비스",
    version="1.0.0",
)

app.include_router(scrape.router)
app.include_router(trafilatura.router)
app.include_router(scrapling.router)


@app.get("/health", tags=["health"], summary="헬스체크")
def health():
    return {"status": "ok"}


# MCP 노출: /scrape 엔드포인트만 도구로 등록
mcp = FastApiMCP(
    app,
    name="Scraper",
    description="웹 페이지 스크래핑 도구",
    include_operations=["scrape"],
)
mcp.mount_http()
