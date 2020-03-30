FROM python

ENV KAGGLE_USERNAME=

COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app

RUN python -m spacy download en_core_web_lg

