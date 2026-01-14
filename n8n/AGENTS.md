# Module Context
**Role:** Workflow automation engine and database.
**Dependencies:** Depends on `postgres` service defined in local `docker-compose.yml`.

# Tech Stack & Constraints
- **Core:** n8n (Docker image).
- **Database:** PostgreSQL.
- **Config:** `.env` for secrets.

# Implementation Patterns
- **Data Persistence:** Uses `./data` for n8n files and `./postgres_data` for database.
- **Network:** Connects to external `server-network`.

# Testing Strategy
- **Verification:** Run `docker compose up -d` locally to test config, but prefer root `./server.sh`.
- **Logs:** Check `docker compose logs -f n8n`.

# Local Golden Rules
## Do's & Don'ts
- **DO** ensure `N8N_SECURE_COOKIE=false` if running over HTTP.
- **DO** keep Postgres credentials consistent between `.env` and `docker-compose.yml`.
- **DO** securely back up `N8N_ENCRYPTION_KEY`.
- **DO** configure log rotation (`max-size: "10m"`) in `docker-compose.yml`.
- **DON'T** commit `.env` or data directories to version control.
