FROM python:3.11-slim

# Install Poetry once and cache it
RUN pip install --no-cache-dir poetry

# Set working directory
WORKDIR /app

# Copy only dependency files first (better caching)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies (no dev packages for production)
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the project
COPY . /app

# Run your main file
CMD ["poetry", "run", "python", "main.py"]
