import xml.etree.ElementTree as ET
import chardet

def ler_primeiras_quatro_linhas(xml_file):
    try:
        print("Tentando abrir o arquivo:", xml_file)
        with open(xml_file, 'rb') as f:
            # Detecta a codificação do arquivo
            encoding = chardet.detect(f.read())['encoding']

        # Abre o arquivo com a codificação detectada
        with open(xml_file, 'r', encoding=encoding) as f:
            print("Arquivo aberto com sucesso.")
            # Lê as quatro primeiras linhas do arquivo XML
            primeira_linha = f.readline().strip()
            segunda_linha = f.readline().strip()
            terceira_linha = f.readline().strip()
            quarta_linha = f.readline().strip()

            # Exibe o conteúdo das quatro primeiras linhas
            print("Primeira linha:", primeira_linha)
            print("Segunda linha:", segunda_linha)
            print("Terceira linha:", terceira_linha)
            print("Quarta linha:", quarta_linha)

    except Exception as e:
        print("Erro ao ler o arquivo XML:", e)

# Caminho para o arquivo XML
xml_file = '/home/alanapaula/Documentos/Mestrado/rejuvenescimento/stackOverFlow/stackoverflow.com-PostHistory/post_history.xml'

# Chama a função para ler as quatro primeiras linhas
ler_primeiras_quatro_linhas(xml_file)
