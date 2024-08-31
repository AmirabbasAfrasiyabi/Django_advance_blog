# Use an official Python runtime as a parent image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY ./core /app/

# Expose the port the app runs on
EXPOSE 8080


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


