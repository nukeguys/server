#!/bin/bash

# 서버 관리 스크립트
# 사용법: ./server.sh [start|stop|restart|status|logs]

set -e
cd "$(dirname "$0")"

NETWORK_NAME="server-network"

# 네트워크 존재 여부 확인 및 생성
ensure_network() {
  if ! docker network inspect "$NETWORK_NAME" >/dev/null 2>&1; then
    echo "🌐 Creating network '$NETWORK_NAME'..."
    docker network create "$NETWORK_NAME"
  fi
}

case "$1" in
  start)
    ensure_network
    echo "🚀 Starting all services..."
    docker compose up -d
    echo "✅ All services started"
    ;;
  stop)
    echo "🛑 Stopping all services..."
    docker compose down
    echo "✅ All services stopped"
    ;;
  restart)
    ensure_network
    echo "🔄 Restarting all services..."
    docker compose down
    docker compose up -d
    echo "✅ All services restarted"
    ;;
  status)
    docker compose ps
    ;;
  logs)
    docker compose logs -f "${@:2}"
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|status|logs [service]}"
    echo ""
    echo "Commands:"
    echo "  start   - Start all services"
    echo "  stop    - Stop all services"
    echo "  restart - Restart all services"
    echo "  status  - Show service status"
    echo "  logs    - Follow logs (optionally specify service)"
    exit 1
    ;;
esac
