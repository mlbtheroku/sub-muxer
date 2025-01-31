FROM python:3.9


COPY . /app
WORKDIR /app
RUN chmod 777 /app
RUN apt -qq update && apt -qq install -y git ffmpeg
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash","start.sh"]
