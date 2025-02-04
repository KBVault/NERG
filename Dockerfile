FROM nikolaik/python-nodejs:python3.10-nodejs19

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/


WORKDIR /app/

RUN pip3 install --no-cache-dir -U -r requirements.txt

RUN chmod +x start

CMD ["python3 -m Devine", "start"]
