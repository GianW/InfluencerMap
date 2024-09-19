# Abre o arquivo para leitura ('r')
with open('./teste.txt', 'r') as file:
    # Lê linha por linha
    for line in file:
        # Exibe cada linha
        print(line, end='')