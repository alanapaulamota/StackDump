def ler_dez_primeiras_linhas(xml_file):
    try:
        with open(xml_file, 'r', encoding='latin1') as f:
            # Lê as dez primeiras linhas do arquivo XML
            linhas = [f.readline().strip() for _ in range(10)]

            # Retorna o conteúdo das dez primeiras linhas
            return linhas

    except Exception as e:
        print("Erro ao ler o arquivo XML:", e)

# Caminho para o arquivo XML
xml_file = '/home/alanapaula/Documentos/Mestrado/rejuvenescimento/stackOverFlow/xml/stackoverflow.com-PostLinks/postLinks.xml'


# Chama a função para ler as dez primeiras linhas
primeiras_dez_linhas = ler_dez_primeiras_linhas(xml_file)

# Exibe o conteúdo das dez primeiras linhas
for i, linha in enumerate(primeiras_dez_linhas, start=1):
    print(f"Linha {i}:", linha)