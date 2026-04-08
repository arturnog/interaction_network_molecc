# A. Seleção de frames
01. Com os arquivos 'prd.tpr' e 'prd.xtc', executar o seguinte comando para coletar os frames para selecionar os mais representativos:

        gmx trjconv -s prd.tpr -f prd.xtc -dt 100 -tu ps -o teste.gro

02. Executar os comandos:

        python3 pca_a.py
        python3 pca_b.py
        python3 pca_c.py

03. Como o arquivo de input para o cálculo das componentes principais 'teste.gro' possui frames a cada 100 ps em uma simulação de 50 ns (50000 ps) (como foi escrito pelo comando gmx trjconv na etapa 01), ao todo o arquivo 'teste.gro' possui 501 frames (contando o frame t=0.000), ordenados de forma cronológica. Dessa maneira, o arquivo 'teste_pca_c.txt' possui 501 pontos com as três componentes principais (PCA1, PCA2, PCA3). Utilizando o Excel, deverá calcular a distância euclidiana para a origem (0, 0, 0), pois os dados foram centralizados na média (pca_b.py), dessa forma os frames mais próximos à origem também são frames mais próximos à média da distribuição. Nesse caso apresentado o tempo de 38.5 ns é considerado ideal.

04. Conhecendo qual(is) é(são) o(s) tempo(s) de simulação do(s) frame(s) representativo(s), separar dos demais por meio do comando:

         gmx trjconv -s prd.tpr -f prd.xtc -b PRIMEIRO -e SEGUNDO -dt 0.1 -o 1_teste.gro -tu ns

05. O comando acima deverá ser rodado da seguinte maneira: com os tempos PRIMEIRO e SEGUNDO diferentes (sendo SEGUNDO o mesmo tempo do frame que se calculará as energias potenciais), com um acréscimo de 0.1 ns, que será usado como input para 'a_water_molecules_generate.py' e 'b_mass_center.py' com objetivo de cálculo do deslocamento dos centros de massas das moléculas e cálculo da energia cinética relativa ao par de moléculas a ponto de considerar interações intermoleculares segundo o critério estabelecido.

         gmx trjconv -s prd.tpr -f prd.xtc -b 38.4 -e 38.5 -dt 0.1 -o 1_teste.gro -tu ns

06. Ao final o arquivo '1_teste_mass_center.txt' terá dois tempos (OK) e o arquivo '1_teste_water_molecules.txt' deverá ser ajustado para ficar só com o tempo de interesse (SEGUNDO) (38.5 ns).
