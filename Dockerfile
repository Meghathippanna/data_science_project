FROM python:3.8-slim-buster
WORKDIR /service
COPY . ./
COPY requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]