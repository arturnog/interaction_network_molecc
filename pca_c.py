# -*- coding: utf-8 -*-

import numpy as np
from sklearn.decomposition import PCA

# Carregar os dados do arquivo input.txt
def carregar_dados(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    dados = [list(map(float, linha.strip().split(';'))) for linha in linhas]
    return np.array(dados)

# Calcular PCA e salvar os resultados
def calcular_pca(arquivo_input, arquivo_output):
    # Carregar os dados
    dados = carregar_dados(arquivo_input)

    # Inicializar o PCA e calcular as componentes
    pca = PCA(n_components=3)
    componentes_principais = pca.fit_transform(dados)

    # Obter a variância explicada em porcentagem
    variancia_explicada = pca.explained_variance_ratio_ * 100

    # Formatar os resultados
    header = f"PC1 ({variancia_explicada[0]:.2f}%)\tPC2 ({variancia_explicada[1]:.2f}%)\tPC3 ({variancia_explicada[2]:.2f}%)\n"

    # Escrever no arquivo de saída
    with open(arquivo_output, 'w') as f:
        f.write(header)
        for linha in componentes_principais:
            f.write(f"{linha[0]}\t{linha[1]}\t{linha[2]}\n")

# Arquivos de entrada e saída
arquivo_input =  'teste_pca_b.txt'
arquivo_output = arquivo_input.replace('_b.txt', '_c.txt')

# Executar o cálculo de PCA
calcular_pca(arquivo_input, arquivo_output)

print(f"PCA calculado e salvo em '{arquivo_output}'!")
