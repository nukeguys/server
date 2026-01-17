# n8n Workflow Automation

n8n 워크플로우 자동화 서비스입니다.

## 접속 URL

| 환경      | URL                   | 비고               |
| :-------- | :-------------------- | :----------------- |
| **Local** | http://localhost:5678 | Mac Mini 로컬 접속 |

## 실행 방법

```bash
# 서버 루트에서 전체 서비스 시작 (권장)
./server.sh start

# 또는 n8n만 개별 실행
cd n8n
docker compose up -d
```

## 환경 변수

| 변수                      | 설명               |
| ------------------------- | ------------------ |
| `N8N_HOST`                | n8n 호스트 도메인  |
| `N8N_PROTOCOL`            | 프로토콜 (https)   |
| `WEBHOOK_URL`             | 웹훅 URL           |
| `N8N_BASIC_AUTH_USER`     | 기본 인증 사용자   |
| `N8N_BASIC_AUTH_PASSWORD` | 기본 인증 비밀번호 |
| `POSTGRES_*`              | PostgreSQL 설정    |

## 백업

```bash
# 데이터 백업
tar -czvf n8n-backup-$(date +%Y%m%d).tar.gz data/ postgres_data/
```

## 컨테이너 구성

- **n8n**: 워크플로우 자동화 (포트 5678)
- **n8n-postgres**: 데이터 저장소
