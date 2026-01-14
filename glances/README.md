# Glances System Monitor

Glances는 시스템 리소스를 모니터링하는 도구입니다.

## 접속 URL

| 환경 | URL |
|------|-----|
| 외부 (Cloudflare) | https://monitor.kkick.xyz |
| 내부 (Tailscale) | http://kkick-mini.tail1c7724.ts.net:61208 |

## 기능
- CPU, Memory, Disk, Network 사용량 모니터링
- Docker 컨테이너 상태 모니터링

## 실행 방법

```bash
# 전체 서비스와 함께 실행 (권장)
cd /Users/kkick/server
./server.sh start

# 개별 실행
cd /Users/kkick/server/glances
docker compose up -d
```

## 모니터링 항목
- **Web UI Mode**: 브라우저에서 접속 가능 (`-w` 옵션)
- **Host PID**: 호스트의 모든 프로세스를 볼 수 있음
- **Docker Socket**: Docker 컨테이너 상태를 볼 수 있음
