# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt  .




# Install the dependencies
RUN pip install  -r requirements.txt


# Copy the rest of the application code into the container
COPY . .
EXPOSE 7002
# Set the command to run the application
CMD ["python","main.py"]