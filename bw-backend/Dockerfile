FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# --app-dir puts src/ on sys.path directly (same convention as pyproject.toml's
# [tool.pytest.ini_options] pythonpath = ["src"]), so main.py's absolute imports
# (e.g. "from api.profesionales import ...") resolve the same way as under pytest.
CMD ["uvicorn", "main:app", "--app-dir", "src", "--host", "0.0.0.0", "--port", "8000"]
