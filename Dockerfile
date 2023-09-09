# Use the official Python image from Docker Hub
FROM python:3.8.10

# Set the working directory to /app
WORKDIR /HNGx

# Copy the current directory contents into the container at /app
COPY . /HNGx

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
