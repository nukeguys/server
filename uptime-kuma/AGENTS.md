# Uptime Kuma

## Overview

- **Role**: Service availability monitoring and alerting
- **Port**: 3001
- **Image**: `louislam/uptime-kuma:1`

## Monitoring Targets

| Service     | Check Type | Internal URL           |
| ----------- | ---------- | ---------------------- |
| n8n         | HTTP       | http://n8n:5678        |
| Open WebUI  | HTTP       | http://open-webui:8080 |
| Vaultwarden | HTTP       | http://vaultwarden:80  |
| Glances     | HTTP       | http://glances:61208   |

## Notification Channels

- Supports Discord, Telegram, Slack, Email, and more
- Configuration: Web UI → Settings → Notifications

## Environment Variables

None (configured via Web UI)

## Volumes

- `./data`: Data storage (monitor settings, history)

## Dependencies

- `server-network`: Communication with other services
