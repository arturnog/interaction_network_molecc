# -*- coding: utf-8 -*-

import re

# Definir as massas dos átomos
mass_O = 2.6568e-23
mass_H = 1.6738e-24
mass_total = mass_O + 2 * mass_H

def parse_coordinates(line):
    #"Extrai as coordenadas dos átomos da linha da molécula."
    #"Retorna um dicionário com as coordenadas de H1, H2 e O."
    pattern = r"H1 \(([\d.,\s\-]+)\) O \(([\d.,\s\-]+)\) .* H2 \(([\d.,\s\-]+)\)"
    match = re.search(pattern, line)
    if match:
        h1 = tuple(map(float, match.group(1).split(',')))
        o = tuple(map(float, match.group(2).split(',')))
        h2 = tuple(map(float, match.group(3).split(',')))
        return {'H1': h1, 'O': o, 'H2': h2}
    return None

def calculate_center_of_mass(coords):
    #Calcula o centro de massa da molécula usando as coordenadas e massas fornecidas.
    h1, o, h2 = coords['H1'], coords['O'], coords['H2']
    cm_x = (mass_H * h1[0] + mass_O * o[0] + mass_H * h2[0]) / mass_total
    cm_y = (mass_H * h1[1] + mass_O * o[1] + mass_H * h2[1]) / mass_total
    cm_z = (mass_H * h1[2] + mass_O * o[2] + mass_H * h2[2]) / mass_total
    return (cm_x, cm_y, cm_z)

# Processar o arquivo
input_file = '1_teste_water_molecules.txt'
output_file = input_file.replace('_water_molecules.txt', '_mass_center.txt')

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    current_time = None

    for line in infile:
        line = line.strip()

        # Identificar tempos
        if line.startswith("Time:"):
            current_time = float(line.split()[1])
            outfile.write("Time: {:.3f}\n".format(current_time))  # Escrever o tempo no formato solicitado

        # Identificar moléculas e coordenadas
        elif line.startswith("W"):
            molecule = line.split(":")[0]
            coords = parse_coordinates(line)

            if coords:
                cm = calculate_center_of_mass(coords)
                outfile.write("{} {:.5f} {:.5f} {:.5f}\n".format(molecule, cm[0], cm[1], cm[2]))

#print("Cálculo completo.")
