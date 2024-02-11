FROM python:3.8.10
WORKDIR /app
COPY . /app
RUN python setup.py install
CMD ["python3", "main.py"]