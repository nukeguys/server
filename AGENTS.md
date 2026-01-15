# Project Context & Operations

**Context:** Mac Mini Home Server (n8n, Cloudflare Tunnel).
**Tech Stack:** Docker Compose, Shell Scripting, n8n, Cloudflare Tunnel.

## Operational Commands
- `./server.sh start` — Start all services (creates network if needed).
- `./server.sh stop` — Stop all services.
- `./server.sh restart` — Restart all services.
- `./server.sh status` — Show status of all containers.
- `./server.sh logs` — View logs for all services.
- `./server.sh logs [service_name]` — View logs for specific service (e.g., `n8n`, `cloudflared`).

# Golden Rules

## Immutable
- **Strict 500-Line Limit:** Keep this and all `AGENTS.md` files under 500 lines.
- **No Emojis:** Use text only.
- **Root Authority:** Using `./server.sh` is the preferred method for managing the full stack.

## Do's & Don'ts
- **DO** use `./server.sh` for global operations to ensure network consistency.
- **DO** keep service-specific configurations in their respective directories.
- **DON'T** modify `docker-compose.yml` files without verifying network settings.
- **DON'T** hardcode secrets; always use `.env` files.

# Standards & References
- **Shell Scripts:** Follow best practices (set -e, proper quoting).
- **Docker:**
  - Use version 2+ compose syntax.
  - **Log Rotation:** Must set `max-size: "10m"` and `max-file: "3"`.
  - **Networking:** Must use `external: true` for `server-network`.
  - **Images:** Use specific version tags or `alpine` variants (no `latest`).

## Maintenance Policy
- Update this file if the global operational script `./server.sh` changes.
- **Change History:** Note reasons for updates at the bottom of files.

# Context Map (Action-Based Routing)

- **[n8n Workflow Automation](./n8n/AGENTS.md)** — Workflow logic, Postgres setup, and n8n configuration.
- **[Cloudflare Tunnel](./cloudflared/AGENTS.md)** — External access configuration and tunnel management.
- **[Open WebUI](./open-webui/AGENTS.md)** — User interface for Local LLM and secret key management.
- **[Ollama (Native)](./ollama/AGENTS.md)** — Native LLM engine configuration and LaunchAgent plist management.
- **[Glances](./glances/AGENTS.md)** — System observability and resource monitoring.
