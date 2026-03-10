import trafilatura
from trafilatura import bare_extraction


def extract_from_url(url: str) -> dict | None:
    """URL에서 본문을 추출한다."""
    downloaded = trafilatura.fetch_url(str(url))
    if not downloaded:
        return None
    return _extract(downloaded, url)


def extract_from_html(html: str, url: str | None = None) -> dict | None:
    """HTML 문자열에서 본문을 추출한다."""
    return _extract(html, url)


def _extract(html: str, url: str | None = None) -> dict | None:
    """Trafilatura로 본문을 추출하는 내부 함수."""
    result = bare_extraction(
        html,
        url=str(url) if url else None,
        include_comments=False,
        include_tables=True,
    )
    if not result or not result.text:
        return None

    return {"text": result.text, "title": result.title}
