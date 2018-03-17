FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN apk --update add curl && rm -rf /var/cache/apk/*
RUN pip install -r requirements.txt
HEALTHCHECK --interval=30s --timeout=3s --start-period=1m --retries=3 CMD curl -f http://localhost:8000/healthcheck || exit 1
CMD ["python", "app.py"]
