FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Setting	Effect
#PYTHONUNBUFFERED=0 (default)	Python buffers output → logs delayed
#PYTHONUNBUFFERED=1	Logs appear instantly → best for Docker apps
ENV PYTHONUNBUFFERED=1 
EXPOSE 8000
CMD ["python", "run.py"]