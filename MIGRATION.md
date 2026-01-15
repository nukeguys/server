# 서버 이전 및 재설치 가이드

서버를 옮기거나 재설치할 때 Docker Compose 실행 전 미리 준비해야 할 사항들입니다.

## 1. 필수 소프트웨어 설치 (OS 레벨)

가장 먼저 기본 도구들을 설치해야 합니다. (Mac/Linux 기준)

### Git
```bash
# Mac (Homebrew)
brew install git
```

### Docker
Docker Desktop for Mac을 설치합니다.
```bash
# Mac (Homebrew)
brew install --cask docker
```
- 설치 후 **Docker 앱을 실행**해야 합니다.

### Tailscale
VPN 구성을 위해 Tailscale을 설치합니다.
```bash
# Mac (Homebrew)
brew install --cask tailscale
```
- **Login**: 앱 실행 후 로그인
- **MagicDNS 확인**: [Tailscale Admin Console](https://login.tailscale.com/admin/dns)에서 MagicDNS 켜짐 확인
- **머신 이름**: 기존과 동일한 도메인(`kkick-mini`)을 쓰려면 Tailscale Admin에서 기존 기기를 제거하거나 이름을 맞춰야 합니다.

### Cloudflared (선택사항)
기본적으로 Docker 컨테이너에서 실행되므로 **호스트 설치는 불필요**합니다.
단, 터널 관리(토큰 발급 등)를 로컬에서 하려면 설치할 수 있습니다:
```bash
brew install cloudflared
```

### Ollama (Native App)
- [ollama.com](https://ollama.com)에서 **공식 앱을 다운로드 및 설치**합니다.
- 설치 후 한 번 실행하여 초기 설정을 완료합니다.

---

## 2. 필수 데이터 백업 & 복원

Docker Compose는 "설정(코드)"만 관리합니다. "데이터"와 "비밀"은 직접 챙겨야 합니다.

### 🔑 환경변수 파일 (`.env`) **[중요!]**
Git에 저장되지 않으므로 **반드시 별도로 백업**해야 합니다.
- `cloudflared/.env` (Tunnel 토큰 포함)
- `n8n/.env` (DB 비밀번호, 암호화 키 포함)
- **복원 방법**: 새 서버의 같은 위치에 파일을 복사합니다.

### 💾 볼륨 데이터 (`data/`)
n8n의 워크플로우 실행 기록, DB 데이터 등은 볼륨 폴더에 저장됩니다.
- `n8n/data/`
- `n8n/postgres_data/`
- **복원 방법**:
  1. 기존 서버에서 압축: `tar -czvf n8n-data.tar.gz n8n/data n8n/postgres_data`
  2. 새 서버로 전송
  3. 압축 해제: `tar -xzvf n8n-data.tar.gz`

### ⚙️ 시스템 설정 (LaunchAgents)
Ollama 공식 앱에 환경 변수를 확실하게 적용(앱 재실행 포함)하기 위한 설정 파일입니다.
- `server/ollama/com.ollama.startup.plist` (저장소에 백업됨)
- **복원 방법**:
  1. `mkdir -p ~/Library/LaunchAgents`
  2. `cp server/ollama/com.ollama.startup.plist ~/Library/LaunchAgents/`
  3. `launchctl load ~/Library/LaunchAgents/com.ollama.startup.plist`

---

## 3. 네트워크 및 외부 접속 설정

### Cloudflare Tunnel
- **설정 불필요**: `cloudflared/.env`에 있는 `CLOUDFLARE_TUNNEL_TOKEN`만 그대로 가져가면, 새 서버에서 실행 즉시 기존 터널에 연결됩니다.
- **주의**: 기존 서버와 새 서버가 동시에 켜져 있으면 충돌 날 수 있으니 기존 서버의 cloudflared는 꺼두세요.

### SSH 키 (GitHub)
`git clone` 또는 `pull`을 위해 SSH 키를 새로 등록해야 할 수 있습니다.
1. 키 생성: `ssh-keygen -t ed25519 -C "your_email@example.com"`
2. 공개키 확인: `cat ~/.ssh/id_ed25519.pub`
3. GitHub > Settings > SSH Keys에 등록

---

## 4. 새 서버에서 실행 순서

1. **소프트웨어 설치** (Git, Docker, Tailscale)
2. **코드 가져오기**: `git clone git@github.com:nukeguys/server.git`
3. **데이터 복원**: `.env` 파일들과 `data/` 폴더 제자리에 복사
4. **네트워크 생성** (스크립트가 자동 처리하지만 수동으로 할 경우):
   ```bash
   docker network create server-network
   ```
5. **서비스 시작**:
   ```bash
   cd server
   ./server.sh start
   ```
