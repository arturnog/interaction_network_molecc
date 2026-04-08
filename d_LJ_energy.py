# -*- coding: utf-8 -*-

import re
import numpy as np

# Constantes
sigma = 0.3159  # nm
epsilon = 0.7749  # KJ mol-1
#avogadro = 6.02214076e23  # mol-1

# Função para calcular V(r)
def lennard_jones_potential(r, sigma, epsilon):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# Função para extrair dados do arquivo e calcular V(r)
def calculate_vr(input_file, output_file, start_time=1.0):
    with open(input_file, 'r') as file:
        data = file.readlines()

    results = []
    current_time = None
    oxygen_positions = {}

    for line in data:
        # Identificar o tempo
        time_match = re.match(r"Time:\s+([\d\.]+)", line)
        if time_match:
            time_value = float(time_match.group(1))
            # Ignorar tempos anteriores ao início
            if time_value < start_time:
                continue

            if current_time is not None and oxygen_positions:
                # Adicionar o tempo no início
                results.append(f"Time: {current_time}\n")
                # Calcular pares de V(r) para o tempo atual
                for i, (mol1, pos1) in enumerate(oxygen_positions.items()):
                    for j, (mol2, pos2) in enumerate(oxygen_positions.items()):
                        if i < j:  # Evitar pares repetidos
                            r = np.linalg.norm(np.array(pos1) - np.array(pos2))
                            v_r = lennard_jones_potential(r, sigma, epsilon)
                            results.append(f"{mol1}, {mol2}, {r:.5f}, {v_r:.5e}\n")

            # Atualizar o tempo e limpar posições
            current_time = time_value
            oxygen_positions = {}
            continue

        # Identificar moléculas e posições dos oxigênios
        mol_match = re.match(r"W(\d+):.*O\s+\(([\d\.\-,\s]+)\)", line)
        if mol_match:
            mol_id = f"W{mol_match.group(1)}"
            pos = list(map(float, mol_match.group(2).split(',')))
            oxygen_positions[mol_id] = pos

    # Processar o último bloco
    if current_time is not None and oxygen_positions:
        results.append(f"Time: {current_time}\n")
        for i, (mol1, pos1) in enumerate(oxygen_positions.items()):
            for j, (mol2, pos2) in enumerate(oxygen_positions.items()):
                if i < j:
                    r = np.linalg.norm(np.array(pos1) - np.array(pos2))
                    v_r = lennard_jones_potential(r, sigma, epsilon)
                    results.append(f"{mol1}, {mol2}, {v_r:.5e}\n")

    # Salvar os resultados
    with open(output_file, 'w') as out_file:
        out_file.writelines(results)

# Arquivos
input_file = "1_teste_water_molecules.txt"
output_file = input_file.replace('_water_molecules.txt', '_LJ.txt')

# Executar o cálculo
calculate_vr(input_file, output_file, start_time=1.0)

print(f"Cálculo completo. Resultados salvos em {output_file}.")
