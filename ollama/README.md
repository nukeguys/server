# Ollama (Native)

이 디렉토리는 Docker 서비스가 아닌 **macOS Native Ollama** 설정을 백업하기 위해 존재합니다.

## 구성 요소
- **`com.ollama.startup.plist`**: 재부팅 시 Ollama를 자동 실행하고 환경 변수를 주입하는 LaunchAgent 파일입니다. (원본은 `~/Library/LaunchAgents/`에 있어야 함)
- **`AGENTS.md`**: 운영 가이드 및 표준.

## 설치 및 복원
[MIGRATION.md](../MIGRATION.md)를 참고하여 `plist` 파일을 `~/Library/LaunchAgents/`로 복사하고 로드해야 합니다.

## 접속 정보

| 환경 | URL | 비고 |
| :--- | :--- | :--- |
| **내부 (Local)** | http://localhost:11434 | API Endpoint |
| **내부 (Tailscale)** | http://kkick-mini.tail1c7724.ts.net:11434 | VPN 내부 API 접근 |
| **외부** | - | 보안상 외부 노출 안 함 |
