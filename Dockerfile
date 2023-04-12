FROM python:3.8
RUN pip install psycopg2
COPY . /app
WORKDIR /app
CMD ["python", "my.py"]