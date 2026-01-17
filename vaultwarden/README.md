# Vaultwarden

Bitwarden 호환 비밀번호 관리자입니다.

## 접속 URL

| 환경      | URL                   | 비고               |
| :-------- | :-------------------- | :----------------- |
| **Local** | http://localhost:3012 | Mac Mini 로컬 접속 |

## 구성 요소

- **`docker-compose.yml`**: 서비스 정의 (메인 `docker-compose.yml`에 include됨)
- **`.env`**: `ADMIN_TOKEN` 등 비밀 정보
- **`data/`**: 비밀번호 저장소

## 실행 방법

```bash
# 서버 루트에서 전체 서비스 시작 (권장)
./server.sh start

# 개별 실행
cd vaultwarden
docker compose up -d
```

## 백업

```bash
# 데이터 백업 (매우 중요!)
tar -czvf vaultwarden-backup-$(date +%Y%m%d).tar.gz data/
```
