# Python Image
FROM python:3.8-alpine

# Maintainer
LABEL maintainer="Po-Yang Chen<poyang31@yahoo.com.tw>"

# Set working directory
WORKDIR /app
COPY . /app

# Initialize working environment
RUN apk add build-base
RUN python setup.py install

# Disable python buffered for display
ENV PYTHONUNBUFFERED true

# Execute Climate
CMD ["python", "main.py"]
