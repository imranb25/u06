
FROM python:3.9


WORKDIR /usr/src/app

COPY . /usr/src/app




CMD ["python", "generate_password.py"]
