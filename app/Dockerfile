FROM python:3.8-alpine3.14

MAINTAINER ashish

RUN mkdir -p /var/app/

WORKDIR /var/app/

COPY . . 

ARG build_date

ENV build_date=${build_date}

RUN pip install -r req.txt

EXPOSE 80

ENTRYPOINT ["python","y42app.py"]
