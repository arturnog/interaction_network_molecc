# -*- coding: utf-8 -*-

import math

def read_coordinates(file_path):
    # Reads the coordinates of water molecules from a file.
    # Returns a dictionary with the corresponding times and coordinates.
    coordinates = {}
    current_time = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('Time:'):
                current_time = float(line.split()[1])  # Get the time
                coordinates[current_time] = []
            elif line:
                parts = line.split()
                molecule = parts[0]
                x, y, z = map(float, parts[1:])
                coordinates[current_time].append((molecule, [x, y, z]))
    return coordinates

# Time interval (dt)
dt = 0.100

def calculate_kinetic_energy(v_i, v_j):
    # Calculates the relative kinetic energy between two molecules.
    # Without NumPy, we calculate the norm manually:
    diff_x = v_i[0] - v_j[0]
    diff_y = v_i[1] - v_j[1]
    diff_z = v_i[2] - v_j[2]
    norm = math.sqrt(diff_x**2 + diff_y**2 + diff_z**2)
    #return (0.5 * 1.49576e-26 / 1000) * norm**2 #kJ
    return (4.50385e-06) * norm**2 #kJ mol-1

def calculate_velocities(coordinates, dt):
    # Calculates the velocities of the molecules based on the coordinates and the time interval.
    velocities = {}
    times = sorted(coordinates.keys())  # Sort the times
    for i in range(1, len(times)):
        current_time = times[i]
        prev_time = times[i - 1]
        # Calculates only if the difference between times is equal to dt
        if abs(current_time - prev_time - dt) < 1e-6:
            for mol, pos in coordinates[current_time]:
                # Checks if the molecule exists at the previous time
                try:
                    prev_pos = next(p for m, p in coordinates[prev_time] if m == mol)
                    # Calculate velocity without NumPy:
                    velocity = [(pos[i] - prev_pos[i]) / dt for i in range(3)]
                    if current_time not in velocities:
                        velocities[current_time] = {}
                    velocities[current_time][mol] = velocity
                except StopIteration:
                    print("The molecule {} is absent at time {}. Ignoring.".format(mol, prev_time))
    return velocities

def is_point_in_cylinder(point, a, b, radius_squared):
    # Cylinder check without NumPy
    ab_x = b[0] - a[0]
    ab_y = b[1] - a[1]
    ab_z = b[2] - a[2]
    ap_x = point[0] - a[0]
    ap_y = point[1] - a[1]
    ap_z = point[2] - a[2]

    t = (ap_x * ab_x + ap_y * ab_y + ap_z * ab_z) / (ab_x**2 + ab_y**2 + ab_z**2)
    t = max(0, min(1, t))  # Clamp t to [0, 1]

    q_x = a[0] + t * ab_x
    q_y = a[1] + t * ab_y
    q_z = a[2] + t * ab_z

    distance_squared = (point[0] - q_x)**2 + (point[1] - q_y)**2 + (point[2] - q_z)**2
    return distance_squared <= radius_squared

def write_kinetic_energy_with_cylinder(output_file, time, velocities, coordinates, radius=0.3159):
    # Optimized with early exit (NumPy removed)
    with open(output_file, 'a') as file:
        file.write("Time: {}\n".format(time))
        molecules = list(velocities.keys())
        coords = {mol: pos for mol, pos in coordinates}
        radius_squared = radius**2  # Pre-calculate squared radius
        for i, mol_i in enumerate(molecules):
            vel_i = velocities[mol_i]
            coord_i = coords[mol_i]
            for mol_j in molecules[i + 1:]:
                vel_j = velocities[mol_j]
                coord_j = coords[mol_j]
                energy = calculate_kinetic_energy(vel_i, vel_j)

                # Check if any other molecule is inside the cylinder
                for mol_k in molecules:
                    if mol_k not in [mol_i, mol_j]:  # Exclude the current pair
                        if is_point_in_cylinder(coords[mol_k], coord_i, coord_j, radius_squared):
                            energy = 1  # Set energy to 1 if inside cylinder
                            break  # Early exit

                file.write("{}, {}, {:.5e}\n".format(mol_i, mol_j, energy))

def main():
    input_file = '1_teste_mass_center.txt'
    output_file = input_file.replace('_mass_center.txt', '_kin_ener.txt')

    # Clear the output file
    with open(output_file, 'w') as file:
        file.truncate(0)

    # Read the coordinates of the molecules
    coordinates = read_coordinates(input_file)
    print("Coordenadas carregadas")  # Modificado para Python 3.5

    # Calculate the velocities
    velocities = calculate_velocities(coordinates, dt)

    # Check if velocities were calculated
    if not velocities:
        print("Nenhuma velocidade foi calculada. Verifique o intervalo de tempo (dt) e os dados de entrada.")
        return

    # Calculate and write the relative kinetic energy for each time
    total_times = len(velocities.keys())
    print("Calculando energias cineticas para {} tempos.".format(total_times))

    # Instead of tqdm, use a simple loop with a counter:
    for i, time in enumerate(sorted(velocities.keys())):
        if time in velocities:
            write_kinetic_energy_with_cylinder(output_file, time, velocities[time], coordinates[time])
        else:
            print("Sem velocidades calculadas para o tempo {}. Pulando.".format(time))
        # Print progress every 100 iterations
        if (i + 1) % 100 == 0:
            print("Processed {} out of {} times".format(i + 1, total_times))

if __name__ == '__main__':
    main()
