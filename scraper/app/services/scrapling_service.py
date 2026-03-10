from scrapling.fetchers import Fetcher, PlayWrightFetcher, StealthyFetcher


def fetch(url: str) -> dict:
    """단순 HTTP 요청으로 HTML을 가져온다."""
    response = Fetcher.get(url)
    return {
        "html": response.html_content,
        "status": response.status,
    }


def dynamic_fetch(url: str, headless: bool = True, wait: float = 0) -> dict:
    """Playwright 기반 DynamicFetcher로 CSR 페이지를 렌더링한다."""
    response = PlayWrightFetcher.fetch(url, headless=headless, wait=wait)
    return {
        "html": response.html_content,
        "status": response.status,
    }


def stealthy_fetch(url: str, headless: bool = True, wait: float = 0) -> dict:
    """Camoufox 기반 StealthyFetcher로 봇 차단을 우회한다."""
    response = StealthyFetcher.fetch(url, headless=headless, wait=wait)
    return {
        "html": response.html_content,
        "status": response.status,
    }
