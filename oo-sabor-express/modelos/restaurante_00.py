
class Restaurante:
    restaurantes = []
    # a função init é o método construtor
    # usamos self pra mostrar que se trata deste objeto
    # semelhante ao 'this' do java
    def __init__(self, nome, categoria):
        # o underline define como privado
        self._nome = nome.title()
        # title faz com que a primeira letra seja maiúscula
        self._categoria = categoria.upper()
        # upper coloca todas as letras em maiúscula
        self._ativo = False
        Restaurante.restaurantes.append(self)
        # append adiciona o restaurante criado a lista 'restaurantes'


    # str mostra o objeto em formato de texto ao invés do endereço de memória
    # semelhante ao método em  java
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    # método para listar os restaurantes
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')



    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo



restaurante_praca = Restaurante('praça', 'Italiana')
restaurante_praca.alternar_estado()
# restaurante_praca.nome = 'Praça'
# restaurante_praca.categoria = 'Italiana'
# restaurante_praca.nome = 'Bistrô'
restaurante_pizza = Restaurante('Pizza Place', 'Fast Food')
# restaurante_pizza.nome = 'Pizza Place'
# restaurante_pizza.categoria = 'Fast Food'
# restaurante_pizza.ativo = True

# print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')

# restaurantes = [restaurante_praca, restaurante_pizza]
# vars mostra o dicionário do objeto
# print(vars(restaurante_praca))
# print(restaurante_pizza)
# dir mostra todos os métodos e atributos
# print(dir(restaurante_pizza))

Restaurante.listar_restaurantes()


