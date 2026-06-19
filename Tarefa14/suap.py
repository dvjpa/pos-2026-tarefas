import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

#user = input("user: ")
#password = getpass()

#data = {"username":user,"password":password}

#response = requests.post(api_url+"token/pair", json=data)
#token = response.json()["access"]
#print(response.json())

token = ""
headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

ano = input("ano: ")
periodo = input("periodo: ")
url = api_url+"ensino/meu-boletim/{ano}/{periodo}/".format(ano=ano, periodo=periodo)
print(url)
response = requests.get(url, headers=headers)

disciplinas =   response.json()["results"]
for Disciplina in disciplinas:
    print(
    f"{Disciplina['disciplina']} -"
    f"{Disciplina['etapa_1']} -"
    f"{Disciplina['etapa_2']} -"
    f"{Disciplina['etapa_3']} -"
    f"{Disciplina['etapa_4']} -"
    )
    

print(response)