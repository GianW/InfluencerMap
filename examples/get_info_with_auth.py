import instaloader
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

def authenticate_instagram(username, password):
    L = instaloader.Instaloader()
    try:
        # Tenta carregar a sessão do arquivo
        L.load_session_from_file(username)
    except FileNotFoundError:
        # Se não encontrar o arquivo, faz login
        L.login(username, password)
        L.save_session_to_file()
    return L


    # # Cria uma instância do Instaloader
    # L = instaloader.Instaloader()

    # # Faz login com as credenciais fornecidas
    # try:
    #     L.login(username, password)
    #     print("Autenticação bem-sucedida!")
    #     return L
    # except instaloader.exceptions.ConnectionException as e:
    #     print(f"Erro de conexão: {e}")
    #     return None
    # except instaloader.exceptions.BadCredentialsException as e:
    #     print(f"Credenciais inválidas: {e}")
    #     return None

def get_profile_data(L, profile_username):
    try:
        # Obtém o perfil usando o nome de usuário
        profile = instaloader.Profile.from_username(L.context, profile_username)

        # Exibe informações do perfil
        print(f"Nome de usuário: {profile.username}")
        print(f"Nome completo: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Seguidores: {profile.followers}")
        print(f"Seguindo: {profile.followees}")
        print(f"Postagens: {profile.mediacount}")
        print(f"URL da imagem do perfil: {profile.profile_pic_url}")
        print(f"É privado: {profile.is_private}")
        print(f"É verificado: {profile.is_verified}")
        print(f"URL externa: {profile.external_url}")
        print(f"É conta de negócios: {profile.is_business_account}")
        print(f"Categoria de negócios: {profile.business_category if profile.is_business_account else 'N/A'}")

        # Listar as contas que o perfil está seguindo
        print("\nContas que estão sendo seguidas:")
        for followee in profile.get_followees():
            print(f"Nome de usuário: {followee.username}")
            print(f"Nome completo: {followee.full_name}")
            print(f"URL do perfil: {followee.profile_pic_url}")
            print(f"Biography: {followee.biography}")
            print(f"Followers Count: {followee.followers}")
            print(f"Following Count: {followee.followees}")
            print(f"Posts Count: {followee.mediacount}")
            print(f"Is Private: {followee.is_private}")
            print(f"Is Verified: {followee.is_verified}")
            print("---" * 5)

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Erro ao obter informações do perfil: {e}")

# Substitua 'your_username' e 'your_password' com suas credenciais do Instagram
if __name__ == "__main__":
    username = os.getenv('USER_NAME')
    password = os.getenv('PASS')
    profile_username = 'shaiross83'  # Substitua pelo nome do perfil que você deseja consultar

    # Autentique e obtenha uma instância autenticada
    L = authenticate_instagram(username, password)

    if L:
        get_profile_data(L, profile_username)
