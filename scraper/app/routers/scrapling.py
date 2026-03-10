import logging

from fastapi import APIRouter, HTTPException

from app.schemas import ScraplingResponse, UrlRequest
from app.services import scrapling_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/scrapling", tags=["scrapling"])


@router.post("/fetch", response_model=ScraplingResponse, summary="단순 HTTP 스크래핑")
def fetch(request: UrlRequest):
    """단순 HTTP 요청으로 HTML을 가져온다."""
    url = str(request.url)
    logger.info("Scrapling fetch: %s", url)

    try:
        result = scrapling_service.fetch(url)
    except Exception as e:
        logger.error("Scrapling fetch 실패: %s", e)
        raise HTTPException(status_code=502, detail=str(e))

    return ScraplingResponse(url=url, **result)


@router.post("/dynamic", response_model=ScraplingResponse, summary="DynamicFetcher 스크래핑")
def dynamic(request: UrlRequest):
    """Playwright 기반 DynamicFetcher로 CSR 페이지를 렌더링한다."""
    url = str(request.url)
    logger.info("Scrapling dynamic: %s", url)

    try:
        result = scrapling_service.dynamic_fetch(url)
    except Exception as e:
        logger.error("Scrapling dynamic 실패: %s", e)
        raise HTTPException(status_code=502, detail=str(e))

    return ScraplingResponse(url=url, **result)


@router.post("/stealthy", response_model=ScraplingResponse, summary="StealthyFetcher 스크래핑")
def stealthy(request: UrlRequest):
    """Camoufox 기반 StealthyFetcher로 봇 차단을 우회한다."""
    url = str(request.url)
    logger.info("Scrapling stealthy: %s", url)

    try:
        result = scrapling_service.stealthy_fetch(url)
    except Exception as e:
        logger.error("Scrapling stealthy 실패: %s", e)
        raise HTTPException(status_code=502, detail=str(e))

    return ScraplingResponse(url=url, **result)
