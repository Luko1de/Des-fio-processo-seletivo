"""Para Encontrar o Logradouro e as demais informações de um Cep pela API via Cep o codigo Cep Precisa estar em um formato de 8 números
sem hifen ou qualquer outro caractere que separe os numeros, como na problemática foi utilizado o hifen irei remover o hifen para que
a consulta seja feita da maneira correta"""

import requests
import csv

#lista de Ceps a serem consultados
ceps = [
    "54767-330", "65065-610", "53150-060", "69910-350",
    "31870-360", "66630-247", "69312-143", "79074-290",
    "69315-255", "87112-567"
]

# url do ViaCEP
url_cep = "https://viacep.com.br/ws/{}/json/"

def consultar_cep(cep):
    url = url_cep.format(cep)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se a resposta tiver um status de erro
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao consultar o CEP {cep}: {e} ele consta como indisponível.")
        return None

# Função para remover o hífen do CEP
def formatar_cep(cep):
    return cep.replace("-", "")

enderecos = []

#Colunas dos dados a serem recebidos pela API
cabecalho = ["CEP", "Logradouro", "Bairro", "Cidade", "Estado"]

# Consultando os CEPs e coletando as informações
for cep in ceps:
    cep_formatado = formatar_cep(cep)
    dados_cep = consultar_cep(cep_formatado)
    if dados_cep and "erro" not in dados_cep:
        logradouro = dados_cep.get("logradouro", "indisponível")
        bairro = dados_cep.get("bairro", "indisponível")
        cidade = dados_cep.get("localidade", "indisponível")
        estado = dados_cep.get("uf", "indisponível")
    else:
        logradouro = "indisponível"
        bairro = "indisponível"
        cidade = "indisponível"
        estado = "indisponível"
    
    enderecos.append([cep, logradouro, bairro, cidade, estado])

# Nome do arquivo CSV
resposta_csv = "enderecos_consultados.csv"

# Escrevendo os dados no arquivo CSV
with open(resposta_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(cabecalho)
    writer.writerows(enderecos)

print(f"Informações dos endereços salvas no arquivo {resposta_csv}.")
