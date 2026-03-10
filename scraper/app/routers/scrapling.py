import logging
from collections.abc import Callable, Coroutine
from typing import Any

from fastapi import APIRouter, HTTPException

from app.schemas import ScraplingResponse, UrlRequest
from app.services import scrapling_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/scrapling", tags=["scrapling"])


async def _handle_fetch(
    url: str,
    method_name: str,
    fetch_fn: Callable[..., Coroutine[Any, Any, dict]],
) -> ScraplingResponse:
    """공통 scrapling fetch 핸들러."""
    logger.info("Scrapling %s: %s", method_name, url)
    try:
        result = await fetch_fn(url)
    except Exception as e:
        logger.error("Scrapling %s 실패: %s", method_name, e)
        raise HTTPException(status_code=502, detail=str(e))
    return ScraplingResponse(url=url, **result)


@router.post("/fetch", response_model=ScraplingResponse, summary="단순 HTTP 스크래핑")
async def fetch(request: UrlRequest):
    """단순 HTTP 요청으로 HTML을 가져온다."""
    return await _handle_fetch(str(request.url), "fetch", scrapling_service.fetch)


@router.post("/dynamic", response_model=ScraplingResponse, summary="DynamicFetcher 스크래핑")
async def dynamic(request: UrlRequest):
    """Playwright 기반 DynamicFetcher로 CSR 페이지를 렌더링한다."""
    return await _handle_fetch(str(request.url), "dynamic", scrapling_service.dynamic_fetch)


@router.post("/stealthy", response_model=ScraplingResponse, summary="StealthyFetcher 스크래핑")
async def stealthy(request: UrlRequest):
    """Camoufox 기반 StealthyFetcher로 봇 차단을 우회한다."""
    return await _handle_fetch(str(request.url), "stealthy", scrapling_service.stealthy_fetch)
