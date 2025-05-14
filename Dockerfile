FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt && pip cache purge

COPY app.py .
ADD templates /app/templates

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
