FROM  python:3.12

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

COPY ./.env ./.env
COPY ./src .

ENTRYPOINT ["python", "main.py"]