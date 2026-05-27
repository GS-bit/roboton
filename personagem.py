from random import randint
from typing import Self

from golpes import GOLPES


class Personagem:
    """
    A classe Personagem representa um Roboton no jogo.
    """

    def __init__(self, nome: str, vida_max: int, ataque: int, defesa: int) -> None:
        self.nome = nome

        self.vida_max = vida_max
        self.vida_atual = vida_max

        self.ataque = ataque
        self.defesa = defesa

        self.condicao = "Normal"  # Pode ser "Normal", "Paralisado", "Congelado" ou "Queimado"

        self.idle = False  # Indica se o personagem pode atacar (True) ou não (False)
        self.idle_turns = 0 # Contador de turnos em que o personagem está ocioso

    def atacar(self, oponente: Self, golpe: str) -> str:
        """
        Reduz a vida de outro personagem atacado pelo próprio personagem.
        Esta função também serve para aplicar os efeitos dos golpes especiais e ofensivos.

        Argumentos:
            oponente: o personagem que está sendo atacado.
            golpe: o nome do golpe a ser utilizado.

        Retorna:
            uma string com logs
        """

        FATOR_MULTIPLICATIVO = 0.3125

        log = ""

        log += f'{self.nome} usou {golpe}!\n'
        oponente.downgrade_vida(FATOR_MULTIPLICATIVO * self.ataque * GOLPES[golpe]["poder"] / oponente.defesa)

        if GOLPES[golpe]["tipo"] == "Ofensivo":
            if golpe == "Arco elétrico" and self.condicao == "Normal" and randint(0, 2) == 0:  # Chance de paralisar o oponente
                oponente.condicao = "Paralisado"
            elif golpe == "Nitrogênio líquido" and self.condicao == "Normal" and randint(0, 2) == 0:  # Chance de congelar o oponente
                oponente.condicao = "Congelado"
            elif golpe == "Sopro de plasma" and self.condicao == "Normal" and randint(0, 2) == 0:  # Chance de queimar o oponente
                oponente.condicao = "Queimado"
        elif GOLPES[golpe]["tipo"] == "Especial":
            if golpe == "Armadura ácida":
                self.defesa *= 1.5
                log += f"A defesa de {self.nome} aumentou!\n"
            elif golpe == "Concentração":
                self.ataque *= 1.5
                log += f"O ataque de {self.nome} aumentou!\n"
            elif golpe == "Renascimento":
                self.upgrade_vida(self.vida_max // 4)
                log += f"A vida de {self.nome} aumentou!\n"
            elif golpe == "Absorver":
                self.upgrade_vida(self.ataque * GOLPES[golpe]["poder"] / oponente.defesa)
                log += f"{self.nome} absorveu vida do oponente!\n"

        return log

    def upgrade_vida(self, incremento: int) -> None:
        """
        Aumenta a vida do personagem.

        Argumentos:
            incremento: a quantidade absoluta de vida a ser adicionada à vida atual.
        """

        nova_vida = self.vida_atual + incremento
        self.vida_atual = min(nova_vida, self.vida_max) # Garante que a vida não ultrapasse o máximo

    def downgrade_vida(self, decremento: int) -> None:
        """
        Reduz a vida do personagem.

        Argumentos:
            decremento: a quantidade absoluta de vida a ser subtraída da vida atual.
        """

        nova_vida = self.vida_atual - decremento
        self.vida_atual = max(nova_vida, 0) # Garante que a vida não fique negativa