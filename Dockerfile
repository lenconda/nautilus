FROM python:3.6-alpine
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN rm -f ./utils/config.py
RUN mv ./utils/config.docker.py ./utils/config.py
CMD ["python", "./run.py"]