# Crawl4AI Service Context

Role: JavaScript-rendered web page crawling API for n8n workflows.
Dependencies: None (standalone service).

## Tech Stack & Constraints

- Core: Crawl4AI server (FastAPI) in Docker.
- Image: unclecode/crawl4ai:0.7.6
- Network: Internal access via server-network. Accessible from n8n as http://crawl4ai:11235.
- Port: 11235 (host) -> 11235 (container).

## API Reference

### Health Check

GET /health

Returns service status.

### Crawl

POST /crawl
Content-Type: application/json

Request Body (URLs):

{
  "urls": ["https://example.com", "https://example.com/about"]
}

Response:

{
  "markdown": "...",
  "metadata": {"title": "..."}
}

### Crawl (Stream)

POST /crawl/stream
Content-Type: application/json

Returns server-sent events for long crawls.

### Markdown

POST /md
Content-Type: application/json

Returns Markdown summarization for crawled pages.
Accepts optional browser/crawler/extraction settings in the request body.

### LLM (Sync)

GET /llm/{url}

Requires model configuration in the service environment.

### LLM (Async)

POST /llm/job
Content-Type: application/json

Queues LLM extraction jobs. Requires model configuration in the service environment.

## Reference

https://docs.crawl4ai.com/api/parameters/
https://docs.crawl4ai.com/core/docker-deployment/

## Implementation Patterns

- Internal Only: No external exposure. Only accessible within server-network.
- Stateless: No persistent data. Can be restarted without data loss.
- n8n Integration: Use HTTP Request node with URL http://crawl4ai:11235/crawl.

## Operational Commands

# Start service
# docker compose up -d

# Check logs
# docker compose logs -f crawl4ai

# Restart service
# docker compose restart crawl4ai

# Test health
# curl http://localhost:11235/health

# Test crawl
# curl -X POST http://localhost:11235/crawl \
#   -H "Content-Type: application/json" \
#   -d '{"urls": ["https://example.com"]}'

## Local Golden Rules

### Do's & Don'ts

- DO use http://crawl4ai:11235 when calling from n8n (container name resolution).
- DO use http://localhost:11235 when testing from host machine.
- DO configure log rotation (max-size: "10m") in docker-compose.yml.
- DON'T expose this service externally (no Cloudflare tunnel needed).
- DON'T hardcode secrets; if LLM keys are needed, add a .llm.env file and wire env_file explicitly.
