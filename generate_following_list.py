import instaloader
import time
from dotenv import load_dotenv
import os
from instagram_utils.auth import login_instaloader
from database_utils import initialize_database, save_profile_data, save_followers_data

load_dotenv()

def get_profile_data(L, conn, profile_username):
    try:
        # Obtém o perfil usando o nome de usuário
        profile = instaloader.Profile.from_username(L.context, profile_username)

        # Salvar dados do perfil no banco de dados
        save_profile_data(conn, profile)

        # Salvar dados dos seguidores no banco de dados
        save_followers_data(conn, profile)

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Erro ao obter informações do perfil: {e}")


if __name__ == "__main__":
    username = os.getenv('USER_NAME')
    password = os.getenv('PASS')
    profile_username = 'shaiross83'  # Perfil a consultar

    conn = initialize_database()

    # Login e obtenção da sessão
    L = login_instaloader(username, password)

    if L:
        get_profile_data(L, conn, profile_username)

    conn.close()
