FROM python:3.9.5
WORKDIR /
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN echo "$CONFIG" >> ./config.json
CMD python3 main.py
