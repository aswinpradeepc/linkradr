# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and to buffer stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Upgrade pip and install the dependencies from the requirements file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 9000

ENTRYPOINT ["./scripts/run.sh"]