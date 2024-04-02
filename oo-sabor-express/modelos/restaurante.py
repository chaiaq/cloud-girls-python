
class Restaurante:
    restaurantes = []
    # a função init é o método construtor
    # usamos self pra mostrar que se trata deste objeto
    # semelhante ao 'this' do java
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    # str mostra o objeto em formato de texto ao invés do endereço de memória
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    # método para listar os restaurantes
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Italiana')
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
print(vars(restaurante_praca))
print(restaurante_pizza)
# dir mostra todos os métodos e atributos
# print(dir(restaurante_pizza))

Restaurante.listar_restaurantes()


