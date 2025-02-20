def ler_dataset(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    cabecalho = linhas[0].strip().split(';')
    dados = [linha.strip().split(';') for linha in linhas[1:] if linha.strip()]
    
    return cabecalho, [linha for linha in dados if len(linha) == len(cabecalho)]

def obter_compositores(dados):
    compositores = sorted(set(linha[4] for linha in dados if len(linha) > 4))  # Verifica se a linha tem a coluna esperada
    return compositores

def distribuir_obras_por_periodo(dados):
    distribuicao = {}
    for linha in dados:
        if len(linha) > 3:
            periodo = linha[3]  # Supondo que o período está na quarta coluna
            distribuicao[periodo] = distribuicao.get(periodo, 0) + 1
    return distribuicao

def obras_por_periodo(dados):
    dicionario = {}
    for linha in dados:
        if len(linha) > 3:
            periodo = linha[3]  # Supondo que o período está na quarta coluna
            titulo = linha[0]  # Supondo que o título está na primeira coluna
            if periodo not in dicionario:
                dicionario[periodo] = []
            dicionario[periodo].append(titulo)
    
    for periodo in dicionario:
        dicionario[periodo].sort()
    
    return dicionario

if __name__ == "__main__":
    nome_arquivo = "obras.csv"  # Substitua pelo nome real do arquivo
    cabecalho, dados = ler_dataset(nome_arquivo)
    
    compositores = obter_compositores(dados)
    distribuicao = distribuir_obras_por_periodo(dados)
    obras_periodo = obras_por_periodo(dados)
    
    print("Lista de compositores ordenada:", compositores)
    print("Distribuição das obras por período:", distribuicao)
    print("Obras organizadas por período:", obras_periodo)