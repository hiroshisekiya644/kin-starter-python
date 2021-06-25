FROM python:3.8

WORKDIR /usr/local/bin

COPY kin.py .
COPY main.py .
COPY requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["python", "main.py"]
