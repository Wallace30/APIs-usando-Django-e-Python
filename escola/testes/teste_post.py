import requests

headers = {'Authorization': 'Token 5ceffd9abc932f06839146675b5782f84e9b7275'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerencia Agil de Projetos Com Scrum",
    "url": "http://www.geekuniversity.com.br/scrum"
}
resultado = requests.post(url =url_base_cursos,headers = headers,data = novo_curso)

# Testando o codigo de status HTTP
assert resultado.status_code == 201


#Testando se o titulo do curso retornado e o memso do informado
assert resultado.json()['titulo'] == novo_curso['titulo']