# Scraper

Trafilatura + Scrapling 통합 웹 스크래핑 API 서비스입니다.

## 주요 기능

- **통합 스크래핑** (`/scrape`): Fallback 로직으로 자동 재시도 (Trafilatura → DynamicFetcher → StealthyFetcher)
- **Trafilatura**: URL/HTML에서 본문 추출
- **Scrapling**: 단순 HTTP, CSR 렌더링, 봇 차단 우회
- **MCP 노출**: `/scrape` 엔드포인트를 MCP 도구로 자동 노출

## 실행

```bash
docker compose up -d --build
```

## API 엔드포인트

| Method | Path | 설명 |
|--------|------|------|
| POST | `/scrape` | Fallback 포함 통합 스크래핑 |
| POST | `/trafilatura/extract` | URL → 본문 추출 |
| POST | `/trafilatura/convert` | HTML → 본문 추출 |
| POST | `/scrapling/fetch` | 단순 HTTP (URL → HTML) |
| POST | `/scrapling/dynamic` | CSR 렌더링 (URL → HTML) |
| POST | `/scrapling/stealthy` | 봇 차단 우회 (URL → HTML) |
| GET | `/health` | 헬스체크 |

## 접속 정보

- **API 문서 (Swagger):** http://localhost:8000/docs
- **MCP 엔드포인트:** http://localhost:8000/mcp
- **내부 접근 (n8n 등):** http://scraper:8000
