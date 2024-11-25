FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

RUN mkdir scripts
COPY ["scripts/predict.py", "./scripts/"]
COPY ["models/mushroom_model.bin", "./models/"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "scripts.predict:app"]