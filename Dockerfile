FROM python:2.7
ENV PYTHONUNBUFFERED 1

ADD setup.py /app/setup.py
RUN cd /app && pip install -e .

ADD . /app

CMD /usr/local/bin/run_crawler
