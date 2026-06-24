FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y default-jdk wget && \
    apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$JAVA_HOME/bin:$PATH

RUN pip install pyspark

WORKDIR /app

COPY . .

RUN mkdir -p output

CMD ["python", "pyspark_app.py"]