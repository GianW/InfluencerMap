import sqlite3

def query_profiles():
    # Conectar ao banco de dados
    conn = sqlite3.connect('instagram_data.db')
    cursor = conn.cursor()

    # Executar uma consulta
    cursor.execute('SELECT * FROM profiles')

    # Recuperar todos os resultados
    profiles = cursor.fetchall()

    # Exibir os resultados
    for profile in profiles:
        print(f"Username: {profile[0]}, Full Name: {profile[1]}, Followers: {profile[3]}, Followees: {profile[4]}")

    # Fechar a conexão
    conn.close()

if __name__ == "__main__":
    query_profiles()
