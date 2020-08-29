FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip; pip install -r requirements.txt
RUN pip install django-bootstrap4
COPY . /code/
