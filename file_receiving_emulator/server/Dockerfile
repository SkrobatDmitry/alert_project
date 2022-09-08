FROM mirekphd/python3.10-ubuntu20.04

RUN mkdir app
WORKDIR ./app
RUN mkdir received_logs
RUN mkdir logs

COPY src .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4455

CMD ["python", "./main.py"]