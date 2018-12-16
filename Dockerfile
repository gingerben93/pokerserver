FROM python:3.7
COPY ./src /app/src
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
EXPOSE 5000
CMD ["python", "/app/src/app.py"]
