FROM python:3.12-slim

WORKDIR /code

# Install dependencies first so this layer is cached between code changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY app ./app

# Cloud platforms inject the port via $PORT; default to 8000 locally
ENV PORT=8000
EXPOSE 8000

# --host '' binds all interfaces on BOTH families (separate IPv4 + IPv6 sockets),
# i.e. dual-stack. --host :: is IPv6-only and 0.0.0.0 is IPv4-only. Dual-stack is
# required on IPv6 clusters where the health probe uses the pod's IPv6 address
# while the in-pod proxy reaches the app over IPv4 loopback.
CMD ["sh", "-c", "uvicorn main:app --host '' --port ${PORT}"]
