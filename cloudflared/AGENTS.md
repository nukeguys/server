# Module Context
**Role:** Secure tunneling for external access (n8n, Chat, Monitor).
**Dependencies:** Connects to Cloudflare Edge.

# Tech Stack & Constraints
- **Core:** cloudflared (Docker image).
- **Config:** `.env` for tunnel token.

# Implementation Patterns
- **Tunneling:** Uses `TUNNEL_TOKEN` from `.env`.
- **Network:** Connects to `server-network` to route traffic to `n8n`, `open-webui`, `glances`.

# Testing Strategy
- **Verification:** Check tunnel status in Cloudflare Dashboard.
- **Logs:** Check `docker compose logs -f cloudflared`.

# Local Golden Rules
## Do's & Don'ts
- **DO** protect the `TUNNEL_TOKEN` at all costs.
- **DO** ensure the container is on the same network (`server-network`) as the services it proxies.
- **DO** use Docker service names (e.g., `open-webui:8080`) for Ingress rules.
- **DO** configure log rotation (`max-size: "10m"`) in `docker-compose.yml`.
- **DO** ensure exposed services are configured with HTTPS in mind.
- **DON'T** expose ports locally unless for debugging; rely on the tunnel.
