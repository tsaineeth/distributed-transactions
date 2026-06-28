FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy workspace metadata
COPY pyproject.toml uv.lock ./
COPY shared ./shared
COPY services/coordinator ./services/coordinator

# Install only the coordinator package and its dependencies
RUN uv sync --package coordinator --frozen

EXPOSE 8000

CMD ["uv", "run", "--package", "coordinator", "uvicorn", "coordinator.main:app", "--host", "0.0.0.0", "--port", "8000"]