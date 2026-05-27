from batalha import Batalha
from heroi import Heroi
from util import clear_screen
from vilao import Vilao

def main() -> None:
    """
    Função principal do jogo, onde os personagens são criados e uma batalha entre eles é realizada.
    """

    clear_screen()
    
    print("ROBOTON")
    input("Pressione Enter para iniciar o jogo...")

    # Batalha:
    Batalha(personagens[0], personagens[1]).iniciar_batalha()

if __name__ == "__main__":
    main()