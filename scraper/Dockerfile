FROM python:3.12-slim

# 시스템 의존성 (Playwright, Camoufox 등에 필요)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Playwright Chromium 설치
RUN playwright install --with-deps chromium

# Camoufox Firefox 브라우저 설치 (StealthyFetcher용)
RUN playwright install-deps firefox && camoufox fetch

# certifi가 시스템 인증서를 사용하도록 심볼릭 링크
RUN CERTIFI_PATH=$(python -c "import certifi; print(certifi.where())") && \
    rm -f "$CERTIFI_PATH" && \
    ln -s /etc/ssl/certs/ca-certificates.crt "$CERTIFI_PATH"

COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
