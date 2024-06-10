import xml.etree.ElementTree as ET

def ler_primeiras_quatro_linhas(xml_file):
    try:
        with open(xml_file, 'r', encoding='latin1') as f:
            # Lê as quatro primeiras linhas do arquivo XML
            primeira_linha = f.readline().strip()
            segunda_linha = f.readline().strip()
            terceira_linha = f.readline().strip()
            quarta_linha = f.readline().strip()

            # Exibe o conteúdo das quatro linhas
            print("Primeira linha:", primeira_linha)
            print("Segunda linha:", segunda_linha)
            print("Terceira linha:", terceira_linha)
            print("Quarta linha:", quarta_linha)

    except Exception as e:
        print("Erro ao ler o arquivo XML:", e)

# Caminho para o arquivo XML
xml_file = '/home/alanapaula/Documentos/Mestrado/rejuvenescimento/stackOverFlow/xml/stackoverflow.com-PostLinks/postLinks.xml'

# Chama a função para ler as quatro primeiras linhas
ler_primeiras_quatro_linhas(xml_file)
