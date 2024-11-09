FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django_advanced/app

COPY requirements.txt /django_advanced/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./django_advanced /django_advanced/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]