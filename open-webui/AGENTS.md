# Open WebUI Service Context

**Role:** User Interface for Local LLM.
**Dependencies:** Requires running Ollama instance (Host).

## Tech Stack & Constraints

- **Core:** Docker (ghcr.io/open-webui/open-webui).
- **Config:** `.env` for secrets (WEBUI_SECRET_KEY).

## Operational Commands

- **Start/Stop:** Managed via root `./server.sh`.
- **Logs:** `./server.sh logs open-webui`.

## Implementation Patterns

- **Host Connection:** Uses `extra_hosts` to map `host.docker.internal` for Ollama access.
- **External Access:** Proxied via Cloudflare Tunnel (`open-webui:8080`).
- **Persistence:** User data stored in `./data`.

## Local Golden Rules

### Do's & Don'ts

- **DO** generate a random `WEBUI_SECRET_KEY` in `.env`.
- **DO** set `OLLAMA_BASE_URL` to `http://host.docker.internal:11434`.
- **DON'T** expose port 8080 externally except via Tunnel.
