FROM python:3.9.9-alpine3.14


# Create a working directory.
RUN mkdir wd
WORKDIR wd

# Install Python dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY script.py .
COPY requirements.txt .

CMD ["python", "-u", "./script.py"]

