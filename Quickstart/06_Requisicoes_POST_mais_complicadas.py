# Tipicamente, você quer enviar algum dado em forma de formulário - assim como um formulário HTML. Para fazer isto,
# simplesmente passe um dicionário para o argumento data. O seu dicionário de dados será automaticamente formatado
# como formulário e a requisição é feita:

import requests, json

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)

print(r.text)

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))

print(r.text)
