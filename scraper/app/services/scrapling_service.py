import asyncio

from playwright.async_api import async_playwright
from scrapling.fetchers import Fetcher, StealthyFetcher

CHALLENGE_MARKERS = (
    "just a moment",
    "performing security verification",
    "enable javascript and cookies to continue",
    "/cdn-cgi/challenge-platform/",
    "challenges.cloudflare.com/turnstile",
    "protect against malicious bots",
)


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


def detect_blocked_response(html: str, status: int | None = None) -> str | None:
    """차단 또는 챌린지 페이지를 감지하면 이유를 반환한다."""
    lowered = html.lower()
    if any(marker in lowered for marker in CHALLENGE_MARKERS):
        return "cloudflare_challenge"
    if status in {401, 403} and "<title>access denied" in lowered:
        return "access_denied"
    return None


async def fetch(url: str) -> dict:
    """단순 HTTP 요청으로 HTML을 가져온다."""
    return await asyncio.to_thread(_fetch_sync, url)


async def dynamic_fetch(url: str, headless: bool = True, wait: float = 0) -> dict:
    """Playwright로 CSR 페이지를 렌더링한다."""
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=headless)
        page = await browser.new_page()
        response = await page.goto(url)
        if wait > 0:
            await page.wait_for_timeout(wait)
        return {"html": await page.content(), "status": response.status if response else None}


async def stealthy_fetch(url: str, headless: bool = True, wait: float = 0) -> dict:
    """Scrapling StealthyFetcher로 페이지를 렌더링한다."""
    return await asyncio.to_thread(_fetch_sync, url, StealthyFetcher, headless=headless, wait=wait)
