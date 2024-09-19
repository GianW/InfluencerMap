import instaloader

# Crie uma instância do Instaloader
L = instaloader.Instaloader()

# Defina a hashtag que você deseja pesquisar
hashtag = '#winnipeg'

try:
    # Crie um objeto Hashtag
    hashtag_obj = instaloader.Hashtag.from_name(L.context, hashtag)
    hashtag_posts = hashtag_obj.get_posts()

    hashtag = Hashtag.from_name(L.context, HASHTAG)

    # Itere sobre as postagens
    for post in hashtag_posts:
        # Exemplo de como acessar dados da postagem
        print(f'Post ID: {post.media_id}')
        print(f'Caption: {post.caption}')
        print(f'Likes: {post.likes}')
        print(f'Comments: {post.comments}')
        print(f'Post Date: {post.date_utc}')
        print('---')

except instaloader.exceptions.QueryReturnedNotFoundException:
    print(f"Erro: Hashtag '{hashtag}' não encontrada ou não acessível.")
except instaloader.exceptions.InstaloaderException as e:
    print(f"Erro: {e}")