# Dockerfile
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variables (if needed)
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the application
CMD ["python", "flask", "run.py", "--host=0.0.0.0", "--port=5000"]