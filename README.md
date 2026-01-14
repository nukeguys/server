# Mac Mini Home Server

Mac Mini 홈 서버 Docker 구성 저장소입니다.

## 사전 준비

> 💡 `server-network`는 `./server.sh start` 실행 시 자동으로 생성됩니다.

> 🚚 **서버 이전/재설치 시**: [MIGRATION.md](MIGRATION.md) 가이드를 참고하세요.


## 서비스 목록

| 서비스 | 설명 | 외부 URL | 내부 URL |
|--------|------|----------|----------|
| n8n | 워크플로우 자동화 | https://n8n.kkick.xyz | http://kkick-mini.tail1c7724.ts.net:5678 |

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

```
server/
├── docker-compose.yml  # 메인 (include)
├── server.sh           # 관리 스크립트
├── cloudflared/
│   ├── docker-compose.yml
│   ├── .env            # cloudflared 환경변수 (git 미추적)
│   └── .env.example
└── n8n/
    ├── docker-compose.yml
    ├── .env            # n8n 환경변수 (git 미추적)
    ├── .env.example
    ├── data/           # n8n 데이터 (git 미추적)
    └── postgres_data/  # DB 데이터 (git 미추적)
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
