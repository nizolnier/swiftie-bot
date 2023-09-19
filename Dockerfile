FROM python:3.9.5
WORKDIR /
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ARG CONFIG
ENV CONFIG=$CONFIG
RUN echo $CONFIG >> ./config.json
RUN cat config.json
CMD python3 main.py
