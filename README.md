# Mac Mini Home Server

Mac Mini 홈 서버 Docker 구성 저장소입니다.

## 사전 준비

> 💡 `server-network`는 `./server.sh start` 실행 시 자동으로 생성됩니다.
>
> 🚚 **서버 이전/재설치 시**: [MIGRATION.md](MIGRATION.md) 가이드 참고

## 보안 및 접속 정책 (Access Policy)

- **공개 서비스**: Cloudflare Tunnel을 통해 외부 도메인으로 접근 가능 (n8n, Vaultwarden 등)
- **내부 서비스 (보통 모니터링)**: **Uptime Kuma, Glances** 등은 보안상 외부로 공개하지 않습니다.
- **원격 접속**: 외부에서 내부 서비스에 접근할 때는 **Tailscale (VPN)**을 사용합니다.
  - Tailscale IP 또는 정해진 MagicDNS 주소를 사용하여 안전하게 접근합니다.

## 서비스 목록

| 서비스          | 설명                   | 내부 URL               |
| :-------------- | :--------------------- | :--------------------- |
| **n8n**         | 워크플로우 자동화      | http://localhost:5678  |
| **Open WebUI**  | 로컬 AI 채팅           | http://localhost:8080  |
| **Ollama**      | AI 모델 엔진 (Native)  | http://localhost:11434 |
| **Glances**     | 시스템 모니터링        | http://localhost:61208 |
| **Vaultwarden** | 비밀번호 관리          | (Tunnel only)          |
| **Uptime Kuma** | 서비스 가용성 모니터링 | http://localhost:3001  |
| **Crawl4AI**    | CSR 페이지 크롤링      | http://localhost:11235 |

## 모니터링 (CLI)

- **Glances**: 시스템 리소스 및 Docker 상태 실시간 확인

  ```bash
  glances
  ```

- **💡 Tip**: 웹 브라우저 접속 없이 터미널(`brew install glances`)에서 바로 확인하는 것이 가장 빠르고 안전합니다.

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
