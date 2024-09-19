# Defina os nomes dos arquivos
arquivos = ['wpgeats.txt', 'wpgeats1.txt', 'wpgeats2.txt']
arquivo_saida = 'seguidores_wpgeats_parcial.txt'

# Conjunto para armazenar linhas únicas
linhas_unicas = set()

# Ler todos os arquivos e adicionar linhas ao conjunto
for nome_arquivo in arquivos:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linhas_unicas.add(linha.strip())  # Remove espaços extras e adiciona ao conjunto

# Escrever as linhas únicas no arquivo de saída
with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
    for linha in sorted(linhas_unicas):  # Ordena as linhas, se desejar
        arquivo.write(linha + '\n')