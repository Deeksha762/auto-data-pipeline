FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything, including data folder
COPY . .

# OR explicitly copy data
# COPY data/ data/
