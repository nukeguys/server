import asyncio

from scrapling.fetchers import Fetcher, PlayWrightFetcher, StealthyFetcher


def _fetch_sync(url: str, fetcher_class=Fetcher, **kwargs) -> dict:
    """Fetcher 클래스로 HTML을 가져오는 공통 동기 함수."""
    if fetcher_class is Fetcher:
        response = fetcher_class.get(url)
    else:
        response = fetcher_class.fetch(url, **kwargs)
    return {
        "html": response.html_content,
        "status": response.status,
    }


async def fetch(url: str) -> dict:
    """단순 HTTP 요청으로 HTML을 가져온다."""
    return await asyncio.to_thread(_fetch_sync, url)


async def dynamic_fetch(url: str, headless: bool = True, wait: float = 0) -> dict:
    """Playwright 기반 DynamicFetcher로 CSR 페이지를 렌더링한다."""
    return await asyncio.to_thread(_fetch_sync, url, PlayWrightFetcher, headless=headless, wait=wait)


async def stealthy_fetch(url: str, headless: bool = True, wait: float = 0) -> dict:
    """Camoufox 기반 StealthyFetcher로 봇 차단을 우회한다."""
    return await asyncio.to_thread(_fetch_sync, url, StealthyFetcher, headless=headless, wait=wait)
