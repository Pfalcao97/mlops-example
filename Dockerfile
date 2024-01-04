# Imagem 3.11 bullseye do Python (versão enxuta)
FROM python:3.11-slim-bullseye

WORKDIR /mlops

COPY . app.py /mlops/

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]