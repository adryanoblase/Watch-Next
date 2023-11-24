FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Download the spaCy model during the Docker build
RUN python -m spacy download en_core_web_md

COPY . .

CMD ["python", "watch_next.py"]
