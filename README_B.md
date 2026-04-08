# B. Criação das redes
* Antes da execução de cada script, verificar e editar o nome do arquivo que será usado como input e o nome do arquivo que será output.

1. Com o arquivo '1_teste.gro' em mãos compreendendo ao frame no tempo escolhido (contendo também um frame com tempo anterior de 0.1 ns), executar os scripts 'a_water_molecules_generate.py' e 'b_mass_center.py', por meio dos comandos:

        python3 a_water_molecules_generate.py
        python3 b_mass_center.py

2. O arquivo '1_teste_mass_center.txt' está ok para prosseguir para as próximas etapas como o cálculo da energia cinética pelo script 'c_kin_energy.py', já o arquivo '1_teste_water_molecules.txt' precisa ser editado, pois possui dois frames, sendo que o interesse é em apenas 1 (no segundo frame), dessa maneira o primeiro frame deverá ser excluído.
