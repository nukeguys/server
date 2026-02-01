# Trafilatura Service Context

**Role:** Web page text extraction API for n8n workflows.
**Dependencies:** None (standalone service).

## Tech Stack & Constraints

- **Core:** Trafilatura (Python library) wrapped in REST API.
- **Image:** `theosun/trafilatura-api:latest` (only `latest` tag available).
- **Network:** Internal access via `server-network`. Accessible from n8n as `http://trafilatura:5000`.
- **Port:** 5001 (host) → 5000 (container).

## API Reference

### Health Check

```
GET /
```

Returns service status.

### Text Extraction

```
POST /extract
Content-Type: application/json
```

**Request Body (URL):**

```json
{
  "url": "https://example.com/article"
}
```

**Request Body (Raw HTML):**

```json
{
  "raw_html": "<html>...</html>"
}
```

**Response:**

```json
{
  "text": "Extracted article text...",
  "title": "Page title",
  "author": "Author name",
  "date": "Publication date"
}
```

## Implementation Patterns

- **Internal Only:** No external exposure. Only accessible within `server-network`.
- **Stateless:** No persistent data. Can be restarted without data loss.
- **n8n Integration:** Use HTTP Request node with URL `http://trafilatura:5000/extract`.

## Operational Commands

```bash
# Start service
docker compose up -d

# Check logs
docker compose logs -f trafilatura

# Restart service
docker compose restart trafilatura

# Test health
curl http://localhost:5001/

# Test extraction
curl -X POST http://localhost:5001/extract \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

## Local Golden Rules

### Do's & Don'ts

- **DO** use `http://trafilatura:5000` when calling from n8n (container name resolution).
- **DO** use `http://localhost:5001` when testing from host machine.
- **DO** configure log rotation (`max-size: "10m"`) in `docker-compose.yml`.
- **DON'T** expose this service externally (no Cloudflare tunnel needed).
- **DON'T** rely on specific image versions (only `latest` is available).
