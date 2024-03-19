FROM python:3.10.12-slim
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
