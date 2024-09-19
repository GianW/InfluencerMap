import sqlite3

def initialize_database():
    # Conectar ao banco de dados (ou criar se não existir)
    conn = sqlite3.connect('instagram_data.db')
    cursor = conn.cursor()

    # Criar tabela para armazenar dados do perfil
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS profiles (
        username TEXT PRIMARY KEY,
        full_name TEXT,
        biography TEXT,
        followers INTEGER,
        followees INTEGER,
        postagens INTEGER,
        private BOOLEAN,
        verified BOOLEAN,
        external_url TEXT,
        is_business_account BOOLEAN,
        business_category TEXT
    )
    ''')
    # (A tabela tem 11 colunas, então deve haver 11 valores no INSERT)

    # Criar tabela para armazenar dados dos seguidores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS followers (
        profile_username TEXT,
        follower_username TEXT,
        full_name TEXT,
        biography TEXT,
        followers_count INTEGER,
        followees_count INTEGER,
        posts_count INTEGER,
        is_private BOOLEAN,
        is_verified BOOLEAN,
        PRIMARY KEY (profile_username, follower_username),
        FOREIGN KEY (profile_username) REFERENCES profiles (username)
    )
    ''')

    conn.commit()
    return conn

def save_profile_data(conn, profile):
    cursor = conn.cursor()

    # Salvar ou atualizar dados do perfil
    cursor.execute('''
    INSERT OR REPLACE INTO profiles (username, full_name, biography, followers, followees,
                                      postagens, private, verified, external_url,
                                      is_business_account, business_category)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (profile.username,
          profile.full_name,
          profile.biography,
          profile.followers,
          profile.followees,
          profile.mediacount,  # A contagem de postagens
          profile.is_private,
          profile.is_verified,
          getattr(profile, 'external_url', None),  # URL externa, se existir
          profile.is_business_account,
          profile.business_category if profile.is_business_account else 'N/A'))

    conn.commit()

def save_followers_data(conn, profile):
    cursor = conn.cursor()

    # Listar as contas que o perfil está seguindo
    count = 0
    print("\nContas que estão sendo seguidas:")
    for followee in profile.get_followees():
        cursor.execute('''
        INSERT OR IGNORE INTO followers (profile_username, follower_username, full_name, biography,
                                          followers_count, followees_count, posts_count, is_private, is_verified)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (profile.username,
              followee.username,
              followee.full_name,
              followee.biography,
              followee.followers,
              followee.followees,
              followee.mediacount,
              followee.is_private,
              followee.is_verified))

        print(f"Nome de usuário: {followee.username}")

        count += 1

        # Pausa a cada 3 perfis processados
        if count % 3 == 0:
            print("Aguardando 10 segundos para evitar bloqueio por automação...")
            time.sleep(10)

    conn.commit()
