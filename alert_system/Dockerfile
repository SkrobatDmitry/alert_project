FROM mirekphd/python3.10-ubuntu20.04

RUN mkdir app
WORKDIR ./app
RUN mkdir logs
RUN mkdir processed_logs

COPY src .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]