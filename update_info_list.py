import instaloader
import time
from instagram_utils.auth import login_instaloader
from dotenv import load_dotenv
import os

# Credenciais Instagram
instagram_username = os.getenv('USER_NAME')
instagram_password = os.getenv('PASS')

def get_profile_followers_with_login(username, L):

    try:
        # Baixa o perfil usando o nome de usuário
        profile = instaloader.Profile.from_username(L.context, username)

        # Obtém o número de seguidores
        followers_count = profile.followers
        print(f"{profile.username} tem {followers_count} seguidores.")
        return f"{profile.username} | {followers_count} | {profile.full_name} | {profile.biography}"

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Erro ao obter informações do perfil: {e}")
        return None

def get_profile_followers(username):
    L = instaloader.Instaloader()

    try:
        # Baixa o perfil usando o nome de usuário
        profile = instaloader.Profile.from_username(L.context, username)

        # Obtém o número de seguidores
        followers_count = profile.followers
        print(f"{profile.username} tem {followers_count} seguidores.")
        return f"{profile.username} | {followers_count} | {profile.full_name} | {profile.biography}"

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Erro ao obter informações do perfil: {e}")
        return None

# Variável para contar o número de perfis processados
count = 0

arquivo_saida = './seguidores_shaiross83_atualizados.txt'

# Login e obtenção da sessão
L = login_instaloader(instagram_username, instagram_password)

with open('./shaiross83.txt', 'r') as file:
    with open(arquivo_saida, 'a', encoding='utf-8') as file_out:
        for line in file:
            # # Atualiza o contador
            count += 1
            # fol = get_profile_followers(line.strip())
            fol = get_profile_followers_with_login(line.strip(), L)
            file_out.write(f"{fol}\n")
            time.sleep(10)

            # Pausa a cada 3 perfis processados
            # if count % 3 == 0:
            #     print("Aguardando 10 segundos para evitar bloqueio por automação...")
            #     time.sleep(10)

