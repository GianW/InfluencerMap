# instagram_utils/auth.py
import instaloader

def login_instaloader(username, password):
    L = instaloader.Instaloader()
    try:
        # Tenta carregar a sessão do arquivo
        L.load_session_from_file(username)
    except FileNotFoundError:
        # Se não encontrar o arquivo, faz login
        L.login(username, password)
        L.save_session_to_file()
    return L
