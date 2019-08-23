FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /tun

RUN pip install pyroute2
COPY . .

CMD ["python", "tun.py"]