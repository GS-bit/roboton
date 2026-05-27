from random import choice


def dialogar() -> str:
    """
    Retorna uma mensagem de um dos Roboton em batalha.
    """

    dialogos = {
        "Benignoton": [
            "Eu sempre busco ajudar os outros e proteger a paz em nosso mundo!",
            "Com minha força e determinação, estou pronto para enfrentar qualquer desafio que surgir!",
            "A bondade supera a maldade, e eu vou provar isso nesta batalha!",
            "O crime é uma mancha que deve ser superada!",
            "Eu acredito que a justiça prevalecerá!",
            "Esta cidade é a minha casa, e eu vou defendê-la com vigor!",
            "O povo desta cidade de Roma deseja a paz!",
            "Fazer o bem é não ser conivente com a injustiça!",
            "Crianças, lembrem-se sempre de obedecer aos seus pais!",
            "Não se deve fazer o mal ao inocente!"
        ],

        "Malignoton": [
            "Mwahaha! Eu sou o Malignoton, o vilão mais malvado e astuto do mundo!",
            "Eu adoro causar caos e destruição por onde passo, e não tenho medo de enfrentar ninguém!",
            "Com minha inteligência e poder, vou espalhar terror, e ninguém poderá me deter!",
            "Este Benignoton não é páreo para mim!",
            "Bondade é fraqueza, maldade é força!",
            "Vem, Benignoton! Você não tem chance contra mim!",
            "A justiça é uma ilusão!",
            "O crime é a verdadeira essência da vida!",
            "Eu vou reduzir Roma a ruínas!",
            "Roma não é nada comparada a mim! Mwahaha!"
        ]
    }

    personagem = choice(["Benignoton", "Malignoton"])
    return f'<b>{personagem}:</b> "{choice(dialogos[personagem])}"'
