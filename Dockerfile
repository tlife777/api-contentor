# Use the official Python image.
# Use python:3.10-slim-buster or similar if you want a lighter image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project code
COPY ./app /app
