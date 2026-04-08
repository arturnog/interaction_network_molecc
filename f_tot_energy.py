import pandas as pd
from tqdm import tqdm

# Carregar os arquivos
coulomb =   pd.read_csv("1_teste_coulomb.txt", sep=",", names=["W_a", "W_b", "Coulomb"])
lj =        pd.read_csv("1_teste_LJ.txt", sep=",", names=["W_a", "W_b", "LJ"])
kin_energ = pd.read_csv("1_teste_kin_ener.txt", sep=",", names=["W_a", "W_b", "Kinetic"])

# Combinar os dados
merged = coulomb.merge(lj, on=["W_a", "W_b"], how="outer").merge(kin_energ, on=["W_a", "W_b"], how="outer")

# Substituir valores ausentes em "Kinetic" por 1
merged["Kinetic"].fillna(1, inplace=True)

# Calcular a soma das energias
for i in tqdm(range(len(merged)), desc="Calculando E_tot"):
    merged.at[i, "Energy_Sum"] = merged.at[i, "Coulomb"] + merged.at[i, "LJ"] + merged.at[i, "Kinetic"] + 0.655 * (22.597)

# Selecionar colunas relevantes para o output
output = merged[["W_a", "W_b", "Energy_Sum"]]

# Salvar o resultado
output.to_csv("1_teste_tot_energy.txt", sep=",", index=False, header=False)

print("Arquivo 'output.txt' gerado com sucesso!")
