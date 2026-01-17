# Open WebUI (Docker)

로컬 LLM을 편리하게 사용하기 위한 Web Interface입니다.

## 구성 요소

- **`docker-compose.yml`**: 서비스 정의. (메인 `docker-compose.yml`에 include됨)
- **`.env`**: `WEBUI_SECRET_KEY` 등 비밀 정보.
- **`data/`**: 사용자 정보 및 채팅 기록 저장소.

## 접속 정보

| 환경      | URL                   | 비고               |
| :-------- | :-------------------- | :----------------- |
| **Local** | http://localhost:8080 | Mac Mini 로컬 접속 |
