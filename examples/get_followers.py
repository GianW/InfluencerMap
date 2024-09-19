import instaloader

def get_profile_followers(username):
    # Cria uma instância do Instaloader
    L = instaloader.Instaloader()

    try:
        # Baixa o perfil usando o nome de usuário
        profile = instaloader.Profile.from_username(L.context, username)

        # Obtém o número de seguidores
        followers_count = profile.followers

        # Exibe o número de seguidores
        print(f"{profile.username} tem {followers_count} seguidores.")
        # print(f"Postagens: {profile.mediacount}") # contagem de posts

         ## Exibe informações do perfil
        # print(f"Nome de usuário: {profile.username}")
        # print(f"Nome completo: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        # print(f"Seguidores: {profile.followers}")
        # print(f"Seguindo: {profile.followees}")
        # print(f"Postagens: {profile.mediacount}")
        # print(f"URL da imagem do perfil: {profile.profile_pic_url}")

        #  ------------------------------------------------
        # Exemplo: Listar as últimas postagens
        # print("\nÚltimas postagens:")
        # for post in profile.get_posts():
        #     print(f"Data: {post.date}")
        #     print(f"Legendas: {post.caption}")
        #     print(f"Curtidas: {post.likes}")
        #     print(f"Comentários: {post.comments}")
        #     print(f"URL da imagem/vídeo: {post.url}")
        #     print("---")

        #  ------------------------------------------------
        # Listar as contas que o perfil está seguindo
        # print("\nContas que estão sendo seguidas:")
        for followee in profile.get_followees():
            print(f"Nome de usuário: {followee.username}")
            print(f"Nome completo: {followee.full_name}")
            print(f"Biography: {followee.biography}")
            print(f"Profile Pic URL: {followee.profile_pic_url}")
            print(f"Followers Count: {followee.followers}")
            print(f"Following Count: {followee.followees}")
            print(f"Posts Count: {followee.mediacount}")
            print(f"Is Private: {followee.is_private}")
            print(f"Is Verified: {followee.is_verified}")
            print(f"URL do perfil: {followee.profile_pic_url}")
            print("---" * 5)

        #  ------------------------------------------------
        # INFOS de contato
        # if profile.is_business_account or profile.is_verified:
        #     print(f"Contato (se disponível): {profile.contact_email if hasattr(profile, 'contact_email') else 'Não disponível'}")
        #     print(f"Telefone (se disponível): {profile.contact_phone if hasattr(profile, 'contact_phone') else 'Não disponível'}")
        # else:
        #     print("Dados de contato não disponíveis para contas pessoais ou não verificadas.")

        #  ------------------------------------------------
        # Verifica se a biografia contém informações de localização
        if 'city' in profile.biography.lower() or 'local' in profile.biography.lower():
            print(f"Possível localização na bio: {profile.biography}")


    except instaloader.exceptions.InstaloaderException as e:
        print(f"Erro ao obter informações do perfil: {e}")

# Substitua 'nome_do_perfil' pelo nome de usuário do Instagram que você deseja consultar
if __name__ == "__main__":
    get_profile_followers('egrid_energia')