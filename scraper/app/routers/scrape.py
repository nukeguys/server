import asyncio
import logging

from fastapi import APIRouter, HTTPException

from app.schemas import ScrapeResponse, UrlRequest
from app.services import scrapling_service, trafilatura_service

logger = logging.getLogger(__name__)
router = APIRouter(tags=["scrape"])


@router.post("/scrape", response_model=ScrapeResponse, summary="통합 스크래핑 (Fallback 포함)", operation_id="scrape")
async def scrape(request: UrlRequest):
    """
    Fallback 흐름:
    1. 단순 HTTP fetch → Trafilatura 본문 추출
    2. DynamicFetcher → Trafilatura 본문 추출
    3. StealthyFetcher → Trafilatura 본문 추출
    """
    url = str(request.url)
    logger.info("통합 스크래핑 시작: %s", url)

    min_text_length = 100
    best = None

    steps = [
        ("http", scrapling_service.fetch),
        ("dynamic", scrapling_service.dynamic_fetch),
        ("stealthy", scrapling_service.stealthy_fetch),
    ]

    for method, fetch_fn in steps:
        try:
            fetched = await fetch_fn(url)
            result = await asyncio.to_thread(trafilatura_service.extract_from_html, fetched["html"], url)
            if not result:
                continue
            response = ScrapeResponse(url=url, method=method, text=result["text"], title=result.get("title"))
            if len(result["text"]) >= min_text_length:
                logger.info("%s 성공: %s", method, url)
                return response
            # 임계값 미달이면 후보로 저장하고 다음 단계 시도
            if not best or len(result["text"]) > len(best.text):
                best = response
            logger.info("%s 텍스트 부족 (%d자), 다음 단계 시도: %s", method, len(result["text"]), url)
        except Exception as e:
            logger.warning("%s 실패: %s - %s", method, url, e)

    if best:
        logger.info("최선 결과 반환 (%s, %d자): %s", best.method, len(best.text), url)
        return best

    logger.error("모든 방법 실패: %s", url)
    raise HTTPException(status_code=502, detail="모든 스크래핑 방법이 실패했습니다.")
