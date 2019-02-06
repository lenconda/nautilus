FROM python:3.6-alpine
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY utils/config.docker.py ./utils/config.py
CMD ["python", "./run.py"]