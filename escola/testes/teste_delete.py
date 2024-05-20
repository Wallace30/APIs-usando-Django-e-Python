import requests

headers = {'Authorization': 'Token 5ceffd9abc932f06839146675b5782f84e9b7275'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url = f'{url_base_cursos}1/',headers=headers)

#Testando o codigo HTTP

assert resultado.status_code == 404

# Testando se o tamanho do conteudo retornado e 0

assert len(resultado.text) == 0