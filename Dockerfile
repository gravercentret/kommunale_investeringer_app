# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Default values for environment variable used in the image
ENV PORT=8000
ENV MAIN_PAGE=webapp/Forside.py
ENV DATABASE_URL=sqlite:///data/data.db

# Define expected mount point for database data file
VOLUME /data

# Expose the port Streamlit runs on
EXPOSE $PORT

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Create a directory for the database and set permissions
RUN mkdir -p /data && chmod -R 755 /data

# Run the Streamlit app
CMD ["/bin/sh", "-c", "streamlit run ${MAIN_PAGE} --server.port=${PORT} --server.address=0.0.0.0"]
