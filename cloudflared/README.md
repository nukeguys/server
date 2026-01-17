# Cloudflare Tunnel

Cloudflare Tunnel을 통해 내부 서비스를 외부에 안전하게 공개합니다.

## 설정된 Public Hostnames

| 서브도메인 | 서비스                 | 비고                         |
| :--------- | :--------------------- | :--------------------------- |
| n8n        | http://n8n:5678        | 워크플로우 자동화            |
| monitor    | http://glances:61208   | 시스템 모니터링 (Email Auth) |
| chat       | http://open-webui:8080 | 로컬 AI 채팅                 |
| vault      | http://vaultwarden:80  | 비밀번호 관리                |

## Tunnel 정보

- **Tunnel 이름**: mini-tunnel
- **관리**: [Cloudflare Zero Trust 대시보드](https://one.dash.cloudflare.com/)

## 새 서비스 공개하기

1. Cloudflare Zero Trust 대시보드 접속
2. Networks → Tunnels → mini-tunnel 선택
3. Public Hostname 추가
   - Subdomain: 원하는 서브도메인
   - Domain: example.com
   - Service: `http://컨테이너명:포트`

> 서비스가 `server-network`에 연결되어 있어야 cloudflared에서 접근 가능

## 보안 설정 (Zero Trust Access)

Glances 등 로그인 기능이 약한 서비스를 외부에 공개할 때는 **Cloudflare Access** 설정을 강력히 권장합니다.

1. **[Zero Trust Dashboard](https://one.dash.cloudflare.com/)** > Access > Applications
2. **Add an application** > Self-hosted 선택
3. **Application Configuration**:
   - Application name: `Monitor` (예시)
   - Domain: `monitor.example.com`
4. **Policies**:
   - Access Policy 생성 (예: `Allow Email`)
   - Action: `Allow`
   - Configure rules: `Emails` 선택 후 본인 이메일 입력
5. 저장하면 해당 도메인 접속 시 이메일 인증이 활성화됩니다.
