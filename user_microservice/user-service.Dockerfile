FROM python:3.9

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6500"]
