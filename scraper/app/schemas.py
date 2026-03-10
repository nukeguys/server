from pydantic import BaseModel, HttpUrl


# 공통
class UrlRequest(BaseModel):
    url: HttpUrl


class HtmlRequest(BaseModel):
    html: str
    url: str | None = None


# /scrape 응답
class ScrapeResponse(BaseModel):
    url: str
    title: str | None = None
    text: str
    method: str  # http, dynamic, stealthy
    success: bool = True


class ErrorResponse(BaseModel):
    url: str
    detail: str
    success: bool = False


# Trafilatura 응답
class TrafilaturaResponse(BaseModel):
    url: str | None = None
    title: str | None = None
    text: str


# Scrapling 응답
class ScraplingResponse(BaseModel):
    url: str
    html: str
    status: int | None = None
