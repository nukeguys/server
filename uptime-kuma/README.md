# Uptime Kuma

서비스 가용성 모니터링 및 알림 도구입니다.

## 접속 URL

| 환경       | URL                     | 비고               |
| :--------- | :---------------------- | :----------------- |
| **Local**  | http://localhost:3001   | Mac Mini 로컬 접속 |
| **Remote** | Tailscale VPN 주소 사용 | 원격 안전 접속     |

> 🔒 **Security Note**: Uptime Kuma는 보안상 외부(Cloudflare)로 공개하지 않으며, 원격지에서는 Tailscale VPN을 통해서만 접근합니다.

## 주요 기능

- HTTP/HTTPS, TCP 포트, Ping, DNS 등 다양한 체크 방식
- Discord, Telegram, Slack, Email 등 다중 알림 채널
- 실시간 상태 대시보드 및 히스토리 그래프
- 한국어 UI 지원

## 실행 방법

```bash
# 서버 루트에서 전체 서비스 시작 (권장)
./server.sh start

# 개별 실행
cd uptime-kuma
docker compose up -d
```

## 초기 설정

1. `http://localhost:3001` 접속
2. 관리자 계정 생성
3. "Add New Monitor" 버튼으로 모니터링 대상 추가

## 백업

```bash
# 데이터 백업
tar -czvf uptime-kuma-backup-$(date +%Y%m%d).tar.gz data/
```
