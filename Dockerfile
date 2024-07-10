# Use a base image of Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the necessary files to the container
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run
ENTRYPOINT ["python3", "forbiddenpass.py"]
