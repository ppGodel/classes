FROM amancevice/pandas:0.25.0-alpine

RUN adduser -D classes

WORKDIR /home/classes

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt && mkdir back_end

COPY app app
COPY ../back_end/web_app back_end/web_app
COPY ../util util
COPY classes_app.py boot.sh waitress_server.py ./
RUN chmod +x boot.sh

RUN chown -R classes:classes ./
USER classes

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]