import logging

from fastapi import APIRouter, HTTPException

from app.schemas import ScrapeResponse, UrlRequest
from app.services import scrapling_service, trafilatura_service

logger = logging.getLogger(__name__)
router = APIRouter(tags=["scrape"])


@router.post("/scrape", response_model=ScrapeResponse, summary="통합 스크래핑 (Fallback 포함)", operation_id="scrape")
def scrape(request: UrlRequest):
    """
    Fallback 흐름:
    1. Trafilatura 단독 (HTTP fetch + 본문 추출)
    2. DynamicFetcher → Trafilatura 본문 추출
    3. StealthyFetcher → Trafilatura 본문 추출
    """
    url = str(request.url)
    logger.info("통합 스크래핑 시작: %s", url)

    # 1단계: Trafilatura 단독
    try:
        result = trafilatura_service.extract_from_url(url)
        if result:
            logger.info("Trafilatura 단독 성공: %s", url)
            return ScrapeResponse(url=url, method="trafilatura", **result)
    except Exception as e:
        logger.warning("Trafilatura 단독 실패: %s - %s", url, e)

    # 2단계: DynamicFetcher → Trafilatura
    try:
        fetched = scrapling_service.dynamic_fetch(url)
        result = trafilatura_service.extract_from_html(fetched["html"], url)
        if result:
            logger.info("DynamicFetcher 성공: %s", url)
            return ScrapeResponse(url=url, method="dynamic", **result)
    except Exception as e:
        logger.warning("DynamicFetcher 실패: %s - %s", url, e)

    # 3단계: StealthyFetcher → Trafilatura
    try:
        fetched = scrapling_service.stealthy_fetch(url)
        result = trafilatura_service.extract_from_html(fetched["html"], url)
        if result:
            logger.info("StealthyFetcher 성공: %s", url)
            return ScrapeResponse(url=url, method="stealthy", **result)
    except Exception as e:
        logger.warning("StealthyFetcher 실패: %s - %s", url, e)

    logger.error("모든 방법 실패: %s", url)
    raise HTTPException(status_code=422, detail="모든 스크래핑 방법이 실패했습니다.")
