# Vaultwarden Service Context

**Context:** Self-hosted Bitwarden-compatible password manager.
**Tech Stack:** Docker, Vaultwarden.

## Operational Commands

- `./server.sh start` — Start all services (from root).
- `./server.sh logs vaultwarden` — View Vaultwarden logs.
- `docker exec -it vaultwarden /bin/sh` — Access container shell.

## Configuration

- **Data Volume:** `./data` — Persistent storage for vault data.
- **External Access:** `https://vault.example.com` via Cloudflare Tunnel.
- **Admin Panel:** `https://vault.example.com/admin` (requires `ADMIN_TOKEN`).

## Do's & Don'ts

- **DO** keep `SIGNUPS_ALLOWED=false` after initial account creation.
- **DO** regularly backup `./data` directory.
- **DON'T** expose the admin panel publicly without HTTPS.
- **DON'T** commit `.env` file to version control.

## Change History

- 2026-01-17: Initial setup.
