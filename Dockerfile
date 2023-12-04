# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV PIP_ROOT_USER_ACTION=ignore

# Define the entry point for the container
CMD python ./main.py
EXPOSE 5000


