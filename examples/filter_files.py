# Filtrar perfis que já estão listados no primeiro arquivo
# Função para extrair o texto antes do pipe de uma linha
def extract_text_before_pipe(line):
    return line.split('|')[0].strip()

# Carregar os textos do segundo arquivo em um conjunto para pesquisa eficiente
def load_texts_from_file(file_path):
    texts = set()
    with open(file_path, 'r') as file:
        for line in file:
            text_before_pipe = extract_text_before_pipe(line)
            texts.add(text_before_pipe)
    return texts

# Processar o primeiro arquivo e remover as linhas que estão no segundo arquivo
def filter_file(input_file_path, output_file_path, texts_to_remove):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            text_before_pipe = extract_text_before_pipe(line)
            if text_before_pipe not in texts_to_remove:
                outfile.write(line)

def main():
    seguidores_1_file = 'seguidores_1_atualizados.txt'
    seguidores_2_file = 'seguidores_2_atualizados.txt'
    filtered_file = 'seguidores_filtrado.txt'

    # Carregar textos do segundo arquivo
    texts_to_remove = load_texts_from_file(seguidores_2_file)

    # Filtrar o primeiro arquivo
    filter_file(seguidores_1_file, filtered_file, texts_to_remove)

if __name__ == "__main__":
    main()
