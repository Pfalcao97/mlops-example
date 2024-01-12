def home():

    return {
        "Apresentação": """Este é um programa básico para 
        apresentar os conceitos introdutório de MLOps."""
    }

def test_home():
    assert home() == {
        "Apresentação": """Este é um programa básico para 
        apresentar os conceitos introdutório de MLOps."""
    }

def sintetize(text: str):

    return {
        "Classificação": 'neutral',
        "Confiança": '100.000%',
    }

def test_sintetize():
    assert sintetize("test") == {
        "Classificação": 'neutral',
        "Confiança": '100.000%',
    }