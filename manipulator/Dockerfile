FROM python:3.9

WORKDIR /app

COPY manipulator/requirements.txt .
RUN pip install -r requirements.txt

COPY manipulator/app.py .

CMD ["python", "app.py"]