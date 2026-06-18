# ==========================================================
# Builder Stage
# ==========================================================
FROM python:3.12-slim AS builder

ENV PIP_NO_CACHE_DIR=1

WORKDIR /build

# Install dependencies first for better layer caching
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt

# Copy application
COPY app ./app


# ==========================================================
# Runtime Stage
# ==========================================================
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create non-root user
RUN groupadd -r appuser && \
    useradd -r -g appuser -d /app -s /sbin/nologin appuser

WORKDIR /app

# Copy installed packages
COPY --from=builder /install /usr/local

# Copy application source
COPY --from=builder /build/app ./app

# Change ownership
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]