# Module Context
**Role:** System Monitoring & Observability.
**Dependencies:** Mounts `/var/run/docker.sock` (Read-only) and `pid: host`.

# Tech Stack & Constraints
- **Core:** Glances (nicolargo/glances).
- **Mode:** Web Server (`-w` flag).
- **Security:** Exposed via Cloudflare Tunnel (`monitor.kkick.xyz`).

# Operational Commands
- **Start/Stop:** Managed via root `./server.sh`.
- **Logs:** `./server.sh logs glances`.

# Implementation Patterns
- **Host Monitoring:** Uses `pid: host` to see all system processes, not just container.
- **Docker Monitoring:** Connects to Docker socket for container stats.
- **Web Interface:** Runs on port 61208.

# Local Golden Rules
## Do's & Don'ts
- **DO** keep the Docker socket read-only (`:ro`).
- **DO** use Cloudflare Access if exposing publicly (sensitive system info).
- **DON'T** remove `pid: host` unless you only want to monitor the container itself.
