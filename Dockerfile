# Imagem 3.11 bullseye do Python (versão enxuta)
FROM python:3.11-slim-bullseye

WORKDIR /mlops

COPY . /mlops/

RUN pip install --no-cache-dir --upgrade -r /mlops/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host",  "0.0.0.0", "--port", "8000"]