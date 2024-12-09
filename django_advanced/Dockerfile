FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

WORKDIR /django_advanced/app

COPY requirements.txt /django_advanced/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./django_advanced /django_advanced/app

EXPOSE ${PORT}

CMD ["watchmedo", "auto-restart", "--directory=.", "--pattern=*.py", "--recursive", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
