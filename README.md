# Mac Mini Home Server

Mac Mini 홈 서버 Docker 구성 저장소입니다.

## 사전 준비

> 💡 `server-network`는 `./server.sh start` 실행 시 자동으로 생성됩니다.
>
> 🚚 **서버 이전/재설치 시**: [MIGRATION.md](MIGRATION.md) 가이드를 참고하세요.

## 서비스 목록

| 서비스          | 설명                  | 내부 URL               |
| :-------------- | :-------------------- | :--------------------- |
| **n8n**         | 워크플로우 자동화     | http://localhost:5678  |
| **Open WebUI**  | 로컬 AI 채팅          | http://localhost:8080  |
| **Ollama**      | AI 모델 엔진 (Native) | http://localhost:11434 |
| **Glances**     | 시스템 모니터링       | http://localhost:61208 |
| **Vaultwarden** | 비밀번호 관리         | http://localhost:3012  |

## 사용법

```bash
# 환경 변수 설정 (각 서비스 폴더에서)
cp 서비스명/.env.example 서비스명/.env
# .env 편집하여 실제 값 입력

# 전체 서비스 시작
./server.sh start

# 전체 서비스 중지
./server.sh stop

# 상태 확인
./server.sh status

# 로그 확인
./server.sh logs [서비스명]
```

## 폴더 구조

모든 서비스는 루트의 `docker-compose.yml`에 의해 통합 관리되며, 각 서비스 디렉토리는 독립적인 **표준 구조**를 따릅니다. 따라서 서비스가 추가되어도 전체 구조의 일관성은 유지됩니다.

```text
server/
├── docker-compose.yml      # 메인 (전체 서비스 조율)
├── server.sh               # 통합 관리 스크립트
└── [서비스명]/              # (예: n8n, open-webui 등)
    ├── docker-compose.yml  # 개별 서비스 정의
    ├── .env                # 비밀 환경변수 (Git 제외, 직접 생성 필요)
    ├── .env.example        # 환경변수 템플릿
    ├── AGENTS.md           # 기술 스택 및 운영 규칙
    └── README.md           # 접속 정보 및 상세 가이드
```

## 새 서비스 추가하기

1. 서비스 폴더 생성: `mkdir 서비스명`
2. `서비스명/docker-compose.yml` 작성 (networks에 아래 추가)

   ```yaml
   networks:
     server-network:
       external: true
   ```

3. `서비스명/.env.example` 및 `.env` 생성
4. `docker-compose.yml`에 include 추가:

   ```yaml
   - path: ./서비스명/docker-compose.yml
     env_file: ./서비스명/.env
   ```

5. Cloudflare 대시보드에서 Public Hostname 추가 (외부 공개 시)
