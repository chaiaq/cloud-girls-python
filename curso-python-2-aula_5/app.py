from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Melancia', 5, 'grande')
prato_paozinho = Prato('Pãozinho', 2, 'Pão com queijo')
restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_bebida_no_cardapio(prato_paozinho)


def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()