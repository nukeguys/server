# Scraper

Trafilatura + Scrapling 통합 웹 스크래핑 API 서비스입니다.

## 주요 기능

- **통합 스크래핑** (`/scrape`): Fallback 로직으로 자동 재시도 (HTTP fetch + Trafilatura 추출 → DynamicFetcher + Trafilatura 추출 → StealthyFetcher + Trafilatura 추출)
- **Trafilatura**: URL/HTML에서 본문 추출
- **Scrapling**: 단순 HTTP, CSR 렌더링, 봇 차단 우회
- **MCP 노출**: `/scrape` 엔드포인트를 MCP 도구로 자동 노출

## 실행

```bash
./server.sh start
```

최초 실행 시 `server-network`는 루트의 [`server.sh`](/Users/kkick/server/server.sh)가 자동으로 생성합니다.

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

## `/scrape` 동작 방식

`/scrape`는 아래 순서로 HTML을 가져오고, 각 단계마다 Trafilatura로 본문을 추출합니다.

1. `scrapling/fetch`로 일반 HTTP 요청
2. 본문 추출 실패 또는 텍스트가 너무 짧으면 `scrapling/dynamic`
3. 그래도 부족하면 `scrapling/stealthy`
4. 텍스트 길이 기준을 넘는 결과를 우선 반환하고, 모두 기준 미달이면 가장 긴 결과를 반환

응답의 `method`는 최종적으로 채택된 단계를 의미하며, 가능한 값은 `http`, `dynamic`, `stealthy`입니다.
Cloudflare 챌린지나 접근 차단 페이지가 감지되면 해당 단계는 실패로 간주하고 다음 단계로 넘어갑니다.

## 요청 / 응답 예시

```bash
curl -X POST http://localhost:8000/scrape \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/article"}'
```

```json
{
  "url": "https://example.com/article",
  "title": "Example Domain",
  "text": "추출된 본문 텍스트...",
  "method": "http",
  "success": true
}
```

`/trafilatura/extract`와 `/trafilatura/convert`는 본문 추출 전용이고, `/scrapling/*` 엔드포인트는 HTML 원문 수집 전용입니다.

모든 단계가 차단 페이지이거나 본문 추출에 실패하면 `/scrape`는 `502 Bad Gateway`를 반환합니다.

## 운영 메모

- 전체 스택 시작/중지/로그 확인은 루트에서 `./server.sh` 사용을 우선합니다.
- 호스트 테스트 URL은 `http://localhost:8000`, 컨테이너 간 호출 URL은 `http://scraper:8000`입니다.
- `dynamic`, `stealthy` 단계는 브라우저 렌더링을 사용하므로 정적 요청보다 느릴 수 있습니다.
- 일부 사이트는 Cloudflare 챌린지나 봇 방어 정책 때문에 우회되지 않을 수 있습니다.

## 접속 정보

- **API 문서 (Swagger):** http://localhost:8000/docs
- **MCP 엔드포인트:** http://localhost:8000/mcp
- **내부 접근 (n8n 등):** http://scraper:8000
