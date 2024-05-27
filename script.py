import requests

def obter_dados_usuario():
    url = "https://randomuser.me/api/"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        
        nome_completo = f"{dados['results'][0]['name']['first']} {dados['results'][0]['name']['last']}"
        genero = dados['results'][0]['gender']
        endereco = f"{dados['results'][0]['location']['street']['number']} {dados['results'][0]['location']['street']['name']}, {dados['results'][0]['location']['city']}, {dados['results'][0]['location']['state']}, {dados['results'][0]['location']['country']}"
        email = dados['results'][0]['email']
        
        print("Informações do usuário aleatório:")
        print(f"Nome completo: {nome_completo}")
        print(f"Gênero: {genero}")
        print(f"Endereço: {endereco}")
        print(f"E-mail: {email}")
        
    except requests.HTTPError as err:
        print(f"Erro HTTP: {err}")
    except requests.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")

if __name__ == "__main__":
    obter_dados_usuario()
