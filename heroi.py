from random import choice

from personagem import Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """

    def __init__(self, nome: str, vida_max: int, ataque: int, defesa: int) -> None:
        super().__init__(nome, vida_max, ataque, defesa)

    def apply_condicao(self) -> str:
        """
        Aplica os efeitos da condição atual do personagem (paralisado, congelado ou queimado).

        Retorna:
            uma string com logs
        """

        log = ""

        if self.condicao == "Paralisado": # O herói tem uma chance de 1/3 de não atacar quando paralisado
            self.idle = False

            if choice([True, False, False]):
                self.idle = True
                log += f'{self.nome} está paralisado e não consegue atacar!\n'
        elif self.condicao == "Congelado": # O herói não ataca quando congelado, mas irá se recuperar dessa condição no terceiro turno
            self.idle = True
            log += f'{self.nome} está congelado e não pode atacar!\n'

            self.idle_turns += 1

            if self.idle_turns == 2:
                self.condicao = "Normal"
                self.idle_turns = 0
                log += f'{self.nome} descongelou e pode atacar novamente!\n'
        elif self.condicao == "Queimado": # O herói perde 5% de sua vida a cada turno quando queimado
            self.downgrade_vida(self.vida_max * 0.05)
            log += f'{self.nome} está sofrendo queimadura!\n'

        return log
