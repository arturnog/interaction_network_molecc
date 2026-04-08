# -*- coding: utf-8 -*-

import numpy as np

def centralizar_na_media(input_file, output_file):
    # Lê os dados do arquivo de entrada
    with open(input_file, 'r') as f:
        data = []
        for line in f:
            # Converte os valores da linha em floats e adiciona à matriz de dados
            row = list(map(float, line.strip().split(';')))
            data.append(row)

    # Converte a matriz de dados para um array NumPy
    data = np.array(data)

    # Calcula a média de cada coluna
    col_means = np.mean(data, axis=0)

    # Centraliza os dados subtraindo a média de cada coluna
    centered_data = data - col_means

    # Salva os dados centralizados em um novo arquivo
    with open(output_file, 'w') as f:
        for row in centered_data:
            f.write(';'.join(f"{value:.6f}" for value in row) + '\n')

# Nome dos arquivos de entrada e saída
input_file =  'teste_pca_a.txt'
output_file = input_file.replace('_a.txt', '_b.txt')

# Executa o processo de centralização
centralizar_na_media(input_file, output_file)