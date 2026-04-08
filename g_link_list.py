
# -*- coding: utf-8 -*-

# Abrir os arquivos
with open('1_teste_tot_energy.txt', 'r') as entrada, open('1_teste_edge_list.txt', 'w') as saida: 
    indice = 1  # Índice para cada conexão

    for linha in entrada:
        linha = linha.strip()

        # Processar apenas linhas que contêm dados
        if linha:
            partes = linha.split(',')
            if len(partes) == 3:
                try:
                    mol1, mol2 = partes[0].strip(), partes[1].strip()
                    energia_total = float(partes[2])  # Converte para float
                    
                    if energia_total < 0:
                        saida.write("{} {} {}\n".format(indice, mol1, mol2))
                        indice += 1
                except ValueError:
                    # Ignora linhas que não possam ser convertidas corretamente
                    continue