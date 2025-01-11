FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV DJANGO_SETTINGS_MODULE=backend.settings
ENV PYTHONUNBUFFERED=1

# Expose the application's port
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]