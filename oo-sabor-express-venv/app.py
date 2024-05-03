import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
# o get solicita um recurso
# nesse caso ele vai pegar a url
# e trabalhar com esses dados

print(response)
# se a resposta for '200' é correto
# esses números são os 'status code'

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
        
    # print(dados_json)
else:
    print(f'O erro foi {response.status_code}')


print(dados_restaurante['McDonald’s'])
