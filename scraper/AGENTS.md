# Scraper Service Context

**Role:** 통합 웹 스크래핑 API 서비스 (Trafilatura + Scrapling).
**Dependencies:** None (standalone service).

## Tech Stack & Constraints

- **Framework:** FastAPI (Python 3.12)
- **본문 추출:** Trafilatura
- **브라우저 크롤링:** Scrapling (PlayWrightFetcher, StealthyFetcher)
- **MCP 노출:** fastapi-mcp
- **Network:** Internal access via `server-network`. Accessible from n8n as `http://scraper:8000`.
- **Port:** 8000 (host) → 8000 (container).

## API Reference

### Health Check

```
GET /health
```

### 통합 스크래핑 (Fallback 포함)

```
POST /scrape
Content-Type: application/json

{"url": "https://example.com/article"}
```

Fallback 순서: HTTP fetch + Trafilatura 추출 → DynamicFetcher + Trafilatura 추출 → StealthyFetcher + Trafilatura 추출

`method`는 최종 성공 단계를 의미하며 값은 `http`, `dynamic`, `stealthy` 중 하나다.

### Trafilatura

```
POST /trafilatura/extract   # URL → 본문 추출
POST /trafilatura/convert   # HTML → 본문 추출
```

### Scrapling

```
POST /scrapling/fetch      # 단순 HTTP (URL → HTML)
POST /scrapling/dynamic    # DynamicFetcher: CSR 렌더링 (URL → HTML)
POST /scrapling/stealthy   # StealthyFetcher: 봇 차단 우회 (URL → HTML)
```

### MCP

- `/mcp` 경로에서 MCP 프로토콜 접근 가능
- `/scrape` 엔드포인트만 MCP 도구로 노출

### Swagger UI

- `/docs` 경로에서 API 문서 확인 가능

## Implementation Patterns

- **Internal Only:** No external exposure. Only accessible within `server-network`.
- **Stateless:** No persistent data. Can be restarted without data loss.
- **n8n Integration:** Use HTTP Request node with URL `http://scraper:8000/scrape`.

## Operational Commands

```bash
# 전체 스택 시작
./server.sh start

# 전체 스택에서 scraper 로그 확인
./server.sh logs scraper

# 전체 스택 재시작
./server.sh restart

# 헬스체크
curl http://localhost:8000/health

# 통합 스크래핑 테스트
curl -X POST http://localhost:8000/scrape \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

## Local Golden Rules

### Do's & Don'ts

- **DO** use `http://scraper:8000` when calling from n8n (container name resolution).
- **DO** use `http://localhost:8000` when testing from host machine.
- **DO** configure log rotation (`max-size: "10m"`) in `docker-compose.yml`.
- **DO** remember that `dynamic` and `stealthy` use browser rendering and can be slower than plain HTTP fetch.
- **DON'T** expose this service externally (no Cloudflare tunnel needed).
