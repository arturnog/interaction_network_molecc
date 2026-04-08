# -*- coding: utf-8 -*-

import math

def calculate_interaction(q_a, q_b, distance):
    epsilon = 5.727657546e-4
    return (q_a * q_b) / (4 * math.pi * epsilon * distance)

def calculate_distance(coord1, coord2):
    return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(coord1, coord2)))

def parse_input_file(filename):
    molecules = {}
    with open(filename, 'r') as file:
        current_time = None
        for line in file:
            line = line.strip()
            if line.startswith("Time:"):
                current_time = float(line.split(":")[1].strip())
            elif line.startswith("W"):
                parts = line.split(":")
                molecule = parts[0].strip()
                coords = parts[1].split(") ")
                parsed_coords = {}
                for coord in coords:
                    if "(" in coord:
                        atom, values = coord.split("(")
                        atom = atom.strip()
                        values = tuple(map(float, values.strip(")").split(", ")))
                        parsed_coords[atom] = values
                molecules[molecule] = parsed_coords
    return current_time, molecules

def calculate_all_interactions(molecules, output_file):
    charges = {'H1': 0.5564, 'H2': 0.5564, 'M': -1.1128, 'O': 0.0}

    # Ordena as chaves extraindo o número da molécula:
    sorted_molecules = sorted(molecules.keys(), key=lambda x: int(x[1:]))

    with open(output_file, 'w') as file:
        for i in range(len(sorted_molecules)):
            mol1 = sorted_molecules[i]
            atoms1 = molecules[mol1]
            for j in range(i + 1, len(sorted_molecules)):
                mol2 = sorted_molecules[j]
                atoms2 = molecules[mol2]
                interactions = []
                total_interaction = 0.0
                for atom1, coord1 in atoms1.items():
                    for atom2, coord2 in atoms2.items():
                        distance = calculate_distance(coord1, coord2)
                        interaction = calculate_interaction(charges[atom1], charges[atom2], distance)
                        interactions.append((atom1, atom2, distance, interaction))
                        total_interaction += interaction
                file.write(f"{mol1}, {mol2}, {total_interaction:.5e}\n")

# Caminho para o arquivo de entrada e saída
input_file = "1_teste_water_molecules.txt"
output_file = input_file.replace('_water_molecules.txt', '_coulomb.txt')

# Processa o arquivo de entrada e calcula interações
time, molecules = parse_input_file(input_file)
calculate_all_interactions(molecules, output_file)

print(f"Interações calculadas e salvas em {output_file}")
