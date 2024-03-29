FROM python:3.8

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]