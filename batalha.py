from random import choice, randint

from dialogos import dialogar
from golpes import GOLPES

class Batalha:
    """
    A classe batalha representa um sistema de batalha entre um herói e um vilão.
    """

    def __init__(self, heroi, vilao) -> None:
        self.heroi = heroi
        self.vilao = vilao

        self.dialogo = dialogar()
        self.log = ""

    def next_turno(self, escolha_do_heroi) -> None:
        """
        Processa o próximo turno da batalha.

        Argumentos:
            escolha_do_heroi: o golpe escolhido pelo herói para atacar o vilão.
        """

        if self.heroi.vida_atual > 0 and self.vilao.vida_atual > 0:
            self.log += self.heroi.apply_condicao()
            self.log += self.vilao.apply_condicao()

            if randint(0,1): # Herói ataca primeiro
                if not self.heroi.idle:
                    self.log += self.heroi.atacar(self.vilao, escolha_do_heroi)

                if self.vilao.vida_atual <= 0:
                    self.log += f'{self.heroi.nome} venceu a batalha!'
                    self.dialogo = "Fim da batalha! Benignoton é o vencedor!"
                    return

                if not self.vilao.idle:
                    escolha_do_vilao = choice(["Arco elétrico", "Disparo sólido", "Nitrogênio líquido", "Sopro de plasma", "Armadura ácida", "Concentração", "Renascimento", "Absorver"])
                    self.log +=self.vilao.atacar(self.heroi, escolha_do_vilao)

                if self.heroi.vida_atual <= 0:
                    self.log += f'{self.vilao.nome} venceu a batalha!'
                    self.dialogo = "Fim da batalha! Malignoton é o vencedor!"
                    return
            else: # Vilão ataca primeiro
                if not self.vilao.idle:
                    escolha_do_vilao = choice(["Arco elétrico", "Disparo sólido", "Nitrogênio líquido", "Sopro de plasma", "Armadura ácida", "Concentração", "Renascimento", "Absorver"])
                    self.log += self.vilao.atacar(self.heroi, escolha_do_vilao)

                if self.heroi.vida_atual <= 0:
                    self.log += f'{self.vilao.nome} venceu a batalha!'
                    self.dialogo = "Fim da batalha! Malignoton é o vencedor!"
                    return

                if not self.heroi.idle:
                    self.log +=self.heroi.atacar(self.vilao, escolha_do_heroi)

                if self.vilao.vida_atual <= 0:
                    self.log += f'{self.heroi.nome} venceu a batalha!'
                    self.dialogo = "Fim da batalha! Benignoton é o vencedor!"
                    return
        else:
            if self.heroi.vida_atual <= 0:
                self.dialogo = "Fim da batalha! Malignoton é o vencedor!"
            else:
                self.dialogo = "Fim da batalha! Benignoton é o vencedor!"