# instagram_utils/profile.py
import instaloader

def get_profile_followers(username, L):
    try:
        # Baixa o perfil usando o nome de usuário
        profile = instaloader.Profile.from_username(L.context, username)
        followers_count = profile.followers
        return followers_count
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Erro ao obter informações do perfil {username}: {e}")
        return None
