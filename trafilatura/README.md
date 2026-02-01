# Trafilatura API

웹 페이지에서 텍스트를 추출하는 API 서비스입니다.

## 용도

- n8n 워크플로우에서 웹 페이지 본문 텍스트 추출
- HTML에서 불필요한 요소(광고, 네비게이션 등) 제거 후 핵심 콘텐츠만 반환

## 접속 URL

| 환경       | URL                       | 비고                      |
| :--------- | :------------------------ | :------------------------ |
| **Local**  | http://localhost:5001     | Mac Mini 로컬 접속        |
| **n8n**    | http://trafilatura:5000   | n8n 컨테이너 내부에서 호출 |

## 실행 방법

```bash
# 서버 루트에서 전체 서비스 시작 (권장)
./server.sh start

# 또는 trafilatura만 개별 실행
cd trafilatura
docker compose up -d
```

## API 엔드포인트

### GET /

헬스체크 엔드포인트입니다.

```bash
curl http://localhost:5001/
```

### POST /extract

웹 페이지 URL 또는 HTML에서 텍스트를 추출합니다.

**URL로 요청:**

```bash
curl -X POST http://localhost:5001/extract \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/article"}'
```

**HTML 직접 전달:**

```bash
curl -X POST http://localhost:5001/extract \
  -H "Content-Type: application/json" \
  -d '{"raw_html": "<html><body><article>본문 내용...</article></body></html>"}'
```

## n8n HTTP Request 노드 설정

| 항목   | 값                             |
| ------ | ------------------------------ |
| Method | POST                           |
| URL    | `http://trafilatura:5000/extract` |
| Body   | JSON                           |

**요청 Body 예시:**

```json
{
  "url": "https://example.com/article"
}
```

**응답 예시:**

```json
{
  "text": "추출된 본문 텍스트...",
  "title": "페이지 제목",
  "author": "작성자",
  "date": "2024-01-01"
}
```

## 컨테이너 구성

- **trafilatura**: 텍스트 추출 API (포트 5000)
