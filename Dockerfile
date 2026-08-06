# Base Image
from python:3.11-slim

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV EURI_API_KEY="euri-c6d35f8e906f8678a928f5c5d474d1ebbe1f3dc791ef3199292fb4af08377ed3"

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit deafult port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501","--server.address=0.0.0.0"]