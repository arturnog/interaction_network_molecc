# B. Criação das redes
# Arquivos iniciais
* Antes da execução de cada script, verificar e editar o nome do arquivo que será usado como input e o nome do arquivo que será output.

1. Com o arquivo '1_teste.gro' em mãos compreendendo ao frame no tempo escolhido (contendo também um frame com tempo anterior de 0.1 ns), executar os scripts 'a_water_molecules_generate.py' e 'b_mass_center.py', por meio dos comandos:

        python3 a_water_molecules_generate.py
        python3 b_mass_center.py

2. O arquivo '1_teste_mass_center.txt' está ok para prosseguir para as próximas etapas como o cálculo da energia cinética pelo script 'c_kin_energy.py', já o arquivo '1_teste_water_molecules.txt' precisa ser editado, pois possui dois frames, sendo que o interesse é em apenas 1 (no segundo frame), dessa maneira o primeiro frame deverá ser excluído.

3. Criar e ativar o ambiente conda contendo as bibliotecas python necessárias: (i) re; (ii) math; (iii) numpy 2.0.2; (iv) pandas 2.2.3; (v) tqdm 4.67.1

# Observações sobre cada script
'c_kinetic_energy.py' - parâmetro $r_c$ do "cilindro de interferência virtual" poderá ser ajeitado nesse script, o defaut é $r_c = \sigma_{OO}$ do modelo TIP4P/2005. Parâmetro dt = 0.1 ns, entre os scripts poderá ser ajustado nesse script, obviamente mantendo coerência com o intervalo entre os dois frames presente no arquivo '1_teste_mass_center.txt'.
'd_LJ_energy.py' - parâmetros de Lennard-Jones $\sigma_{OO}$ e $\epsilon_{OO}$ deverão ser ajustados caso o modelo de água seja diferente de TIP4P/2005.
'e_Coulomb.py' - parâmetros das cargas atômicas deverão ser ajustadas conforme modelo, bem como a existência ou ausência do sítio M.
'g_tot_energy.py' - ajeitar o parâmetro $4 * E^H_{Kin}$ como a energia cinética dos átomos de H seguindo a distribuição de Maxwell-Boltzmann.

# Execução
4. Ativar e executar o script 'executar_todos.sh' através dos seguintes comandos:

        chmod +x executar_todos.sh
        ./executar_todos.sh

5. O arquivo '1_teste_edge_list.txt' lista todas as interações existentes e quais nós compreendem às respectivas arestas.
