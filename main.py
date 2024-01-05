"""
Aplicativo simples em Flask utilizado para demonstrar 
conceitos introdutórios de MLOps.
"""

from fastapi import FastAPI
from transformers import pipeline

# https://huggingface.co/citizenlab/twitter-xlm-roberta-base-sentiment-finetunned
MODEL_PATH = "citizenlab/twitter-xlm-roberta-base-sentiment-finetunned"
SENTIMENT_DICT = {"Neutral": "Neutro", "Positive": "Positivo", "Negative": "Negativo"}

app = FastAPI()


@app.get("/")
def home():
    """
    Endpoint inicial.
    """

    return {
        "Apresentação": """Este é um programa básico para 
        apresentar os conceitos introdutório de MLOps."""
    }


@app.get("/sintetize/{text}")
def sintetize(text: str):
    """
    Endpoint de análise de sentimento. Análise da entonação de uma frase.
    Como usar:

    Ao chamar o endpoint com a frase 'Eu estou adorando aprender sobre MLOps!',
    você recebe o seguinte resultado:

    {
        "Classificação": "Positivo",
        "Confiança": "99.191%"
    }
    """

    sentiment_classifier = pipeline(
        "text-classification", model=MODEL_PATH, tokenizer=MODEL_PATH
    )

    return {
        "Classificação": SENTIMENT_DICT[sentiment_classifier(text)[0]["label"]],
        "Confiança": f"{100*sentiment_classifier(text)[0]['score'] :.3f}%",
    }
