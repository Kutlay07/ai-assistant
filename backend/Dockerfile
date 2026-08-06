FROM python:3.13-slim AS builder

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -e .



FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]