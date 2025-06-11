FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install boto3
CMD ["python", "ai_agent.py"]
