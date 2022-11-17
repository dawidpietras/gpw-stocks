FROM python:latest

WORKDIR /workdir

COPY ./requirements.txt /workdir
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /workdir

CMD ["pytest", "tests/test_db.py"]

