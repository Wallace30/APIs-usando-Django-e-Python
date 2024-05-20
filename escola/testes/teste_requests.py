import requests

# GET Avaliações

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o codigo de status HTTP
# print(avaliacoes.status_code)

#Acessando os dados da resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json()))

# Acessando a quantidade de registros
#print(avaliacoes.json()['count'])

#Proxima pagina de registros
#print(avaliacoes.json()['next'])

#Acessando os resultados dessa pagina
#print(avaliacoes.json()['results'])

#Acessando o primeiro elemento da lista
#print(avaliacoes.json()['results'][0])


# GET Cursos
headers = {'Authorization': 'Token 5ceffd9abc932f06839146675b5782f84e9b7275'}

cursos = requests.get(url ='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())