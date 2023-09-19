FROM python:3.9.5
WORKDIR /
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD python3 main.py
