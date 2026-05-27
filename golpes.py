"""
Este arquivo contém todos os golpes disponíveis no jogo.
"""

GOLPES = {
    "Arco elétrico": {
        "tipo": "Ofensivo",
        "poder": 50,
        "desc": "Um arco elétrico que eletrifica o alvo. Pode paralisar o oponente."
    },

    "Disparo sólido": {
        "tipo": "Ofensivo",
        "poder": 100,
        "desc": "Um disparo sólido que perfura a blindagem do alvo."
    },

    "Nitrogênio líquido": {
        "tipo": "Ofensivo",
        "poder": 50,
        "desc": "Nitrogênio líquido gélido. Pode congelar o oponente."
    },

    "Sopro de plasma": {
        "tipo": "Ofensivo",
        "poder": 50,
        "desc": "Um sopro de plasma superaquecido. Pode queimar o oponente."
    },

    "Armadura ácida": {
        "tipo": "Especial",
        "poder": 0,
        "desc": "Aumenta a defesa do personagem em 50%."
    },

    "Concentração": {
        "tipo": "Especial",
        "poder": 0,
        "desc": "Aumenta o ataque do personagem em 50%."
    },

    "Renascimento": {
        "tipo": "Especial",
        "poder": 0,
        "desc": "Aumenta o HP do personagem em 1/4 do seu valor máximo."
    },

    "Absorver": {
        "tipo": "Especial",
        "poder": 25,
        "desc": "Aumenta o HP do personagem com o dano sofrido pelo oponente."
    },
}