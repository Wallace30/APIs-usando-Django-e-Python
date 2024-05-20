import requests

headers = {'Authorization': 'Token 5ceffd9abc932f06839146675b5782f84e9b7275'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo":"Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}
#Buscando curso com id 6
#curso = requests.get(url = f'{url_base_cursos}1/',headers=headers)
#print(curso.json())
resultado = requests.put(url = f'{url_base_cursos}1/',headers=headers,data = curso_atualizado )

# Testando o codigo de status HTTP
#assert resultado.status_code == 200

#Testando o titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']