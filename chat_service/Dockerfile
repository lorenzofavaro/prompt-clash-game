# Build stage
FROM python:3.9.2-slim AS builder

# Install poetry
RUN pip install poetry==2.0.1

# Configure poetry (to not create a virtual environment)
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Set working directory
WORKDIR /app

# Copy the poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies without the source code
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# Final stage
FROM python:3.9.2-slim AS runtime

# Set working directory
WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Copy the virtual environment from builder
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Copy the source code
COPY . .

# Expose Uvicorn port
EXPOSE 8000

# Start Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
