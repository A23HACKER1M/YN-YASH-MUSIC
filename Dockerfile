FROM nikolaik/python-nodejs:python3.10-nodejs17
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /VIVI/
WORKDIR /VIVI/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD bash start
