# Use an official Python base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy your app code into container
COPY . /app

# Install Flask inside container
RUN pip install flask

# Tell Docker how to run your app
CMD ["python", "app.py"]
