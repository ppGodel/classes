FROM python:3.6-alpine

RUN adduser -D classes

WORKDIR /home/classes

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY back_app back_app
COPY util util
COPY classes_app.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP classes_app.py

RUN chown -R classes:classes ./
USER classes

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]