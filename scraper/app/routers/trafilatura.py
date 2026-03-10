import logging

from fastapi import APIRouter, HTTPException

from app.schemas import HtmlRequest, TrafilaturaResponse, UrlRequest
from app.services import trafilatura_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/trafilatura", tags=["trafilatura"])


@router.post("/extract", response_model=TrafilaturaResponse, summary="URL에서 본문 추출")
def extract(request: UrlRequest):
    """Trafilatura로 URL에서 본문을 추출한다."""
    url = str(request.url)
    logger.info("Trafilatura extract: %s", url)

    result = trafilatura_service.extract_from_url(url)
    if not result:
        raise HTTPException(status_code=502, detail="본문을 추출할 수 없습니다.")

    return TrafilaturaResponse(url=url, text=result["text"], title=result.get("title"))


@router.post("/convert", response_model=TrafilaturaResponse, summary="HTML에서 본문 추출")
def convert(request: HtmlRequest):
    """Trafilatura로 HTML 문자열에서 본문을 추출한다."""
    logger.info("Trafilatura convert: html_length=%d", len(request.html))

    result = trafilatura_service.extract_from_html(request.html, request.url)
    if not result:
        raise HTTPException(status_code=422, detail="본문을 추출할 수 없습니다.")

    return TrafilaturaResponse(url=request.url, text=result["text"], title=result.get("title"))
