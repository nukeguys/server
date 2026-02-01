# Crawl4AI API

CSR(클라이언트 사이드 렌더링) 페이지까지 크롤링하는 API 서비스입니다.

## 용도

- n8n 워크플로우에서 JS 렌더링 페이지 크롤링
- SPA/CSR 페이지의 본문 수집

## 접속 URL

| 환경      | URL                      | 비고                 |
| :-------- | :----------------------- | :------------------- |
| Local     | http://localhost:11235   | Mac Mini 로컬 접속   |
| n8n       | http://crawl4ai:11235    | n8n 컨테이너 내부 호출 |

## 실행 방법

```bash
# 서버 루트에서 전체 서비스 시작 (권장)
./server.sh start

# 또는 crawl4ai만 개별 실행
cd crawl4ai
docker compose up -d
```

## API 엔드포인트

### GET /health

헬스체크 엔드포인트입니다.

```bash
curl http://localhost:11235/health
```

### POST /crawl

URL 배열을 전달하면 페이지들을 크롤링합니다.

```bash
curl -X POST http://localhost:11235/crawl \
  -H "Content-Type: application/json" \
  -d '{\"urls\": [\"https://example.com\", \"https://example.com/about\"]}'
```

### POST /crawl/stream

긴 크롤링 작업을 스트리밍으로 받습니다.

```bash
curl -N -X POST http://localhost:11235/crawl/stream \
  -H "Content-Type: application/json" \
  -d '{\"urls\": [\"https://example.com\", \"https://example.com/about\"]}'
```

### POST /md

크롤링 결과를 Markdown으로 정리해 반환합니다. 필요 시 옵션을 함께 전달해
브라우저/크롤러/추출 동작을 조정할 수 있습니다.

```bash
curl -X POST http://localhost:11235/md \
  -H "Content-Type: application/json" \
  -d '{\"urls\": [\"https://example.com\"]}'
```

### GET /llm/{url}

LLM 추출 결과를 반환합니다. 모델 설정이 필요합니다.

```bash
curl \"http://localhost:11235/llm/https%3A%2F%2Fexample.com\"
```

### POST /llm/job

LLM 추출 작업을 비동기로 큐에 넣습니다. 모델 설정이 필요합니다.

```bash
curl -X POST http://localhost:11235/llm/job \
  -H \"Content-Type: application/json\" \
  -d '{\"urls\": [\"https://example.com\"]}'
```

## 옵션/스키마 참고

`/md`, `/crawl`, `/crawl/stream`, `/llm/job`는 공통적으로 브라우저/크롤러/추출 설정을
요청 바디에 포함할 수 있습니다. 상세 옵션 목록과 예시는 공식 문서를 참고하세요.

```text
https://docs.crawl4ai.com/api/parameters/
https://docs.crawl4ai.com/core/docker-deployment/
https://docs.crawl4ai.com/core/self-hosting/
```

## n8n HTTP Request 노드 설정

| 항목   | 값                            |
| ------ | ----------------------------- |
| Method | POST                          |
| URL    | `http://crawl4ai:11235/crawl` |
| Body   | JSON                          |

요청 Body 예시:

```json
{
  "urls": ["https://example.com"]
}
```

## 컨테이너 구성

- crawl4ai: JS 렌더링 크롤링 API (포트 11235)
