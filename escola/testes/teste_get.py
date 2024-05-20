import requests

headers = {'Authorization': 'Token 5ceffd9abc932f06839146675b5782f84e9b7275'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url = url_base_cursos, headers = headers)
#print(resultado.json())
#Testando se o endpoint esta correto
assert resultado.status_code == 200
