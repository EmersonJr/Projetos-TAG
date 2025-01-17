# Trabalho 2 - Emparelhamento estável maxímo

<h2>⌨️ Autores</h2>
<ul>
  <li>Isabela Souza Sisnando de Araujo - 231018884</li>
  <li>Emerson Luiz Cruz Junior - 231003531</li>
</ul>
<table>
  <tr>
    <td align="center"><a href="https://github.com/isasisnando" target="_blank"><img style="border-radius: 50%;" src="https://github.com/isasisnando.png" width="100px;" alt="Isa Souza"/><br /><sub><b>Isa Souza</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/EmersonJr" target="_blank"><img style="border-radius: 50%;" src="https://github.com/EmersonJr.png" width="100px;" alt="Emerson Junior"/><br /><sub><b>Emerson Junior</b></sub></a><br /></td>
</table>

## Rodando o codígo:

Para rodar o codígo inicialmente é necessário compilar e gerar um executável, isso pode ser feito executando o seguinte comando:

```shell
g++ main.cpp -o main
```
Com o codígo compilado e o executável gerado, execute o programa com:

```shell
./main
```

## O problema:

O problema proposto consiste em encontrar um emparelhamento estável e máximo para a atribuição de alunos a projetos.

Cada aluno recebe uma nota, calculada com base em seu histórico e tempo disponível. Além disso, os alunos apresentam uma lista com até três projetos, ordenada por ordem de preferência, aos quais têm interesse em se vincular. 

Para os projetos, são especificadas a nota mínima exigida e a capacidade máxima de participantes. Os responsáveis pelos projetos buscam selecionar os alunos com as maiores notas, priorizando, portanto, aqueles que apresentam melhor desempenho nas métricas definidas.

## A solução
A solução para o problema foi elaborada com base no algoritmo Gale-Shapely, uma vez que o objetivo do trabalho é encontrar o emparelhamento entre 
projetos e alunos.
O algoritmo adaptado funciona da seguinte maneira:
- Cria-se uma fila com todos os alunos, e enquanto essa fila não está vazia:
	- retira-se o aluno da frente na fila
	- analisa-se o primeiro projeto que o aluno ainda não tentou participar e está na sua lista
	- caso o aluno não tenha nota suficiente para o projeto, ele entra na fila novamente para que o próximo projeto na sua lista seja analisado
	- caso contrário:
		- se há vagas no projeto, realiza-se o emparelhamento do projeto com aluno
		- se todas as vagas estão ocupadas, verifica-se se o aluno possui nota maior do que algum dos alunos que está no projeto, nesse caso, o aluno entra na vaga
e o outro aluno é retirado do projeto (possivelmente é colocado novamente na fila se ainda há projetos para analisar na sua lista)

Os responsáveis pelo projeto optaram por realizar uma otimização, a qual consiste em não adicionar um aluno a fila de alunos caso ele não possua nota o suficiente para entrar em nenhum dos projetos em sua lista, visto que não seria aceito em nenhum projeto, mesmo se houvesse vaga.

Seguindo os requisitos do trabalho, o algoritmo é rodado 10 vezes , buscando atingir a melhor aproximação do emparelhamento maxímo, alterando aleatoriamente a ordem em que os alunos são colocados na fila em cada iteração.

A aproximação final é obtida considerando o maior emparelhamento encontrado durante as 10 iterações .

## Resultados:

Os resultados das 10 iterações e o emparelhamento maxímo obtidos em nossa execução estarão disponíveis aqui, possivelmente ao executar um resultado diferente possa ser obtido, uma vez que o programa utiliza uma função aleatória para ordenar os alunos na fila.

### Primeira iteração:
```shell
Iteração 1
Inserindo o par : Projeto P40  Aluno A26
Inserindo o par : Projeto P24  Aluno A114
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P36  Aluno A56
Inserindo o par : Projeto P41  Aluno A27
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P43  Aluno A153
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P36  Aluno A92
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P38  Aluno A62
Inserindo o par : Projeto P26  Aluno A98
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P21  Aluno A147
Inserindo o par : Projeto P26  Aluno A142
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P30  Aluno A160
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P37  Aluno A61
Inserindo o par : Projeto P41  Aluno A47
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P39  Aluno A63
Retirando o par: Projeto P41 Aluno A47
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P1  Aluno A200
Retirando o par: Projeto P30 Aluno A160
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P35  Aluno A175
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P8  Aluno A188
Retirando o par: Projeto P5 Aluno A185
Inserindo o par : Projeto P5  Aluno A85
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P7  Aluno A187
Retirando o par: Projeto P41 Aluno A27
Inserindo o par : Projeto P41  Aluno A197
Inserindo o par : Projeto P20  Aluno A52
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P3  Aluno A44
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P17  Aluno A161
Retirando o par: Projeto P40 Aluno A26
Inserindo o par : Projeto P40  Aluno A84
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P9  Aluno A66
Retirando o par: Projeto P3 Aluno A44
Inserindo o par : Projeto P3  Aluno A100
Retirando o par: Projeto P21 Aluno A147
Inserindo o par : Projeto P21  Aluno A157
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P25  Aluno A134
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P51  Aluno A96
Retirando o par: Projeto P20 Aluno A52
Inserindo o par : Projeto P20  Aluno A64
Inserindo o par : Projeto P50  Aluno A1
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A177
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P23  Aluno A197
Retirando o par: Projeto P25 Aluno A134
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P55  Aluno A26
58 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A161 P18-A177 P2-A32 P20-A64 P21-A157 P22-A144 P23-A197 P24-A114 P25-A84 P26-A142 P26-A98 P27-A81 P27-A83 P28-A127 P29-A163 P3-A100 P3-A33 P30-A64 P34-A174 P35-A175 P36-A56 P36-A92 P37-A61 P38-A62 P39-A63 P4-A34 P40-A84 P41-A107 P41-A197 P43-A153 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A35 P5-A85 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Segunda iteração:
```shell
Iteração 2
Inserindo o par : Projeto P36  Aluno A68
Inserindo o par : Projeto P37  Aluno A177
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P26  Aluno A142
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P24  Aluno A141
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P30  Aluno A164
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P17  Aluno A161
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P35  Aluno A175
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P36  Aluno A168
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P38  Aluno A62
Retirando o par: Projeto P30 Aluno A164
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P7  Aluno A187
Inserindo o par : Projeto P40  Aluno A6
Inserindo o par : Projeto P26  Aluno A143
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P41  Aluno A27
Inserindo o par : Projeto P43  Aluno A196
Inserindo o par : Projeto P21  Aluno A145
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P3  Aluno A4
Inserindo o par : Projeto P20  Aluno A52
Retirando o par: Projeto P17 Aluno A161
Inserindo o par : Projeto P17  Aluno A61
Retirando o par: Projeto P3 Aluno A4
Inserindo o par : Projeto P3  Aluno A100
Retirando o par: Projeto P21 Aluno A145
Inserindo o par : Projeto P21  Aluno A157
Retirando o par: Projeto P20 Aluno A52
Inserindo o par : Projeto P20  Aluno A64
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A157
58 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A61 P18-A157 P2-A32 P20-A64 P21-A157 P22-A144 P23-A197 P24-A141 P25-A84 P26-A142 P26-A143 P27-A81 P27-A83 P28-A127 P29-A163 P3-A100 P3-A33 P30-A64 P34-A174 P35-A175 P36-A168 P36-A68 P37-A177 P38-A62 P39-A63 P4-A34 P40-A6 P41-A107 P41-A27 P43-A196 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Terceira iteração:
```shell
Iteração 3
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P24  Aluno A91
Inserindo o par : Projeto P41  Aluno A47
Inserindo o par : Projeto P38  Aluno A62
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P36  Aluno A68
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P26  Aluno A98
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P41  Aluno A7
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P21  Aluno A145
Inserindo o par : Projeto P37  Aluno A61
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P36  Aluno A168
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P40  Aluno A6
Inserindo o par : Projeto P43  Aluno A153
Inserindo o par : Projeto P26  Aluno A48
Inserindo o par : Projeto P30  Aluno A133
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P35  Aluno A175
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P2  Aluno A32
Retirando o par: Projeto P30 Aluno A133
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P7  Aluno A187
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P48  Aluno A85
Retirando o par: Projeto P41 Aluno A47
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P17  Aluno A161
Inserindo o par : Projeto P20  Aluno A141
Retirando o par: Projeto P21 Aluno A145
Inserindo o par : Projeto P21  Aluno A157
Inserindo o par : Projeto P3  Aluno A94
Retirando o par: Projeto P41 Aluno A7
Inserindo o par : Projeto P41  Aluno A107
Retirando o par: Projeto P3 Aluno A94
Inserindo o par : Projeto P3  Aluno A100
Retirando o par: Projeto P20 Aluno A141
Inserindo o par : Projeto P20  Aluno A64
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A177
57 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A161 P18-A177 P2-A32 P20-A64 P21-A157 P22-A144 P23-A197 P24-A91 P25-A84 P26-A48 P26-A98 P27-A81 P27-A83 P28-A127 P29-A163 P3-A100 P3-A33 P30-A64 P34-A174 P35-A175 P36-A168 P36-A68 P37-A61 P38-A62 P39-A63 P4-A34 P40-A6 P41-A107 P43-A153 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Quarta iteração:
```shell
Iteração 4
Inserindo o par : Projeto P30  Aluno A160
Inserindo o par : Projeto P43  Aluno A153
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P7  Aluno A187
Inserindo o par : Projeto P37  Aluno A177
Inserindo o par : Projeto P35  Aluno A55
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P26  Aluno A143
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P36  Aluno A168
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P36  Aluno A68
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P24  Aluno A114
Inserindo o par : Projeto P41  Aluno A7
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P38  Aluno A100
Inserindo o par : Projeto P21  Aluno A147
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P26  Aluno A142
Inserindo o par : Projeto P41  Aluno A47
Inserindo o par : Projeto P40  Aluno A6
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P4  Aluno A34
Retirando o par: Projeto P30 Aluno A160
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P17  Aluno A161
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P25  Aluno A84
Retirando o par: Projeto P41 Aluno A47
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P20  Aluno A52
Retirando o par: Projeto P21 Aluno A147
Inserindo o par : Projeto P21  Aluno A137
Inserindo o par : Projeto P3  Aluno A4
Retirando o par: Projeto P17 Aluno A161
Inserindo o par : Projeto P17  Aluno A61
Retirando o par: Projeto P41 Aluno A7
Inserindo o par : Projeto P41  Aluno A107
Retirando o par: Projeto P20 Aluno A52
Inserindo o par : Projeto P20  Aluno A64
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A157
57 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A61 P18-A157 P2-A32 P20-A64 P21-A137 P22-A144 P23-A197 P24-A114 P25-A84 P26-A142 P26-A143 P27-A81 P27-A83 P28-A127 P29-A163 P3-A33 P3-A4 P30-A64 P34-A174 P35-A55 P36-A168 P36-A68 P37-A177 P38-A100 P39-A63 P4-A34 P40-A6 P41-A107 P43-A153 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Quinta iteração:
```shell
Iteração 5
Inserindo o par : Projeto P40  Aluno A106
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P36  Aluno A128
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P30  Aluno A164
Inserindo o par : Projeto P26  Aluno A98
Inserindo o par : Projeto P37  Aluno A137
Inserindo o par : Projeto P38  Aluno A100
Retirando o par: Projeto P30 Aluno A164
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P43  Aluno A196
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P21  Aluno A147
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P7  Aluno A187
Inserindo o par : Projeto P36  Aluno A68
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P3  Aluno A4
Inserindo o par : Projeto P35  Aluno A175
Inserindo o par : Projeto P24  Aluno A141
Inserindo o par : Projeto P26  Aluno A143
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P41  Aluno A97
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P20  Aluno A152
Retirando o par: Projeto P21 Aluno A147
Inserindo o par : Projeto P21  Aluno A177
Inserindo o par : Projeto P17  Aluno A61
Retirando o par: Projeto P20 Aluno A152
Inserindo o par : Projeto P20  Aluno A64
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A157
58 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A61 P18-A157 P2-A32 P20-A64 P21-A177 P22-A144 P23-A197 P24-A141 P25-A84 P26-A143 P26-A98 P27-A81 P27-A83 P28-A127 P29-A163 P3-A33 P3-A4 P30-A64 P34-A174 P35-A175 P36-A128 P36-A68 P37-A137 P38-A100 P39-A63 P4-A34 P40-A106 P41-A107 P41-A97 P43-A196 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Sexta iteração:
```shell
Iteração 6
Inserindo o par : Projeto P41  Aluno A97
Inserindo o par : Projeto P43  Aluno A46
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P38  Aluno A100
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P35  Aluno A55
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P36  Aluno A56
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P26  Aluno A143
Inserindo o par : Projeto P36  Aluno A68
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P37  Aluno A157
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P24  Aluno A114
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P17  Aluno A61
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P26  Aluno A142
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P40  Aluno A106
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P3  Aluno A4
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P21  Aluno A147
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P41  Aluno A27
Retirando o par: Projeto P41 Aluno A97
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P7  Aluno A187
Inserindo o par : Projeto P20  Aluno A172
Retirando o par: Projeto P41 Aluno A27
Inserindo o par : Projeto P41  Aluno A107
Retirando o par: Projeto P21 Aluno A147
Inserindo o par : Projeto P21  Aluno A137
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A177
57 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A61 P18-A177 P2-A32 P20-A172 P21-A137 P22-A144 P23-A197 P24-A114 P25-A84 P26-A142 P26-A143 P27-A81 P27-A83 P28-A127 P29-A163 P3-A33 P3-A4 P30-A64 P34-A174 P35-A55 P36-A56 P36-A68 P37-A157 P38-A100 P39-A63 P4-A34 P40-A106 P41-A107 P43-A46 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Sétima iteração:
```shell
Iteração 7
Inserindo o par : Projeto P40  Aluno A106
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P38  Aluno A62
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P43  Aluno A46
Inserindo o par : Projeto P41  Aluno A97
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P37  Aluno A177
Inserindo o par : Projeto P30  Aluno A164
Inserindo o par : Projeto P24  Aluno A141
Inserindo o par : Projeto P36  Aluno A68
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P36  Aluno A168
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P26  Aluno A142
Inserindo o par : Projeto P3  Aluno A4
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P26  Aluno A98
Inserindo o par : Projeto P20  Aluno A172
Inserindo o par : Projeto P41  Aluno A47
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P6  Aluno A8
Retirando o par: Projeto P41 Aluno A97
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P35  Aluno A55
Inserindo o par : Projeto P45  Aluno A155
Retirando o par: Projeto P30 Aluno A164
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P17  Aluno A61
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P21  Aluno A147
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P7  Aluno A187
Retirando o par: Projeto P41 Aluno A47
Inserindo o par : Projeto P41  Aluno A107
Retirando o par: Projeto P21 Aluno A147
Inserindo o par : Projeto P21  Aluno A137
Retirando o par: Projeto P3 Aluno A4
Inserindo o par : Projeto P3  Aluno A100
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A157
Retirando o par: Projeto P20 Aluno A172
Inserindo o par : Projeto P20  Aluno A64
57 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A61 P18-A157 P2-A32 P20-A64 P21-A137 P22-A144 P23-A197 P24-A141 P25-A84 P26-A142 P26-A98 P27-A81 P27-A83 P28-A127 P29-A163 P3-A100 P3-A33 P30-A64 P34-A174 P35-A55 P36-A168 P36-A68 P37-A177 P38-A62 P39-A63 P4-A34 P40-A106 P41-A107 P43-A46 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Oitava iteração:
```shell
Iteração 8
Inserindo o par : Projeto P43  Aluno A196
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P38  Aluno A100
Inserindo o par : Projeto P36  Aluno A168
Inserindo o par : Projeto P7  Aluno A187
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P36  Aluno A56
Inserindo o par : Projeto P40  Aluno A6
Inserindo o par : Projeto P17  Aluno A61
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P37  Aluno A137
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P24  Aluno A191
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P41  Aluno A97
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P26  Aluno A143
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P30  Aluno A164
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P35  Aluno A55
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P21  Aluno A147
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P22  Aluno A144
Retirando o par: Projeto P30 Aluno A164
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P26  Aluno A98
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P3  Aluno A4
Inserindo o par : Projeto P20  Aluno A52
Retirando o par: Projeto P21 Aluno A147
Inserindo o par : Projeto P21  Aluno A157
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A177
Retirando o par: Projeto P20 Aluno A52
Inserindo o par : Projeto P20  Aluno A64
58 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A61 P18-A177 P2-A32 P20-A64 P21-A157 P22-A144 P23-A197 P24-A191 P25-A84 P26-A143 P26-A98 P27-A81 P27-A83 P28-A127 P29-A163 P3-A33 P3-A4 P30-A64 P34-A174 P35-A55 P36-A168 P36-A56 P37-A137 P38-A100 P39-A63 P4-A34 P40-A6 P41-A107 P41-A97 P43-A196 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Nona iteração:
```shell
Iteração 9
Inserindo o par : Projeto P40  Aluno A106
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P43  Aluno A196
Inserindo o par : Projeto P36  Aluno A128
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P7  Aluno A187
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P24  Aluno A114
Inserindo o par : Projeto P15  Aluno A14
Inserindo o par : Projeto P36  Aluno A92
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P35  Aluno A55
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P30  Aluno A160
Inserindo o par : Projeto P41  Aluno A27
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P37  Aluno A137
Inserindo o par : Projeto P21  Aluno A145
Inserindo o par : Projeto P3  Aluno A4
Inserindo o par : Projeto P38  Aluno A100
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P26  Aluno A142
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P26  Aluno A98
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P12  Aluno A31
Retirando o par: Projeto P30 Aluno A160
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P17  Aluno A61
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P20  Aluno A72
Retirando o par: Projeto P21 Aluno A145
Inserindo o par : Projeto P21  Aluno A177
Retirando o par: Projeto P20 Aluno A72
Inserindo o par : Projeto P20  Aluno A64
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A157
58 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A61 P18-A157 P2-A32 P20-A64 P21-A177 P22-A144 P23-A197 P24-A114 P25-A84 P26-A142 P26-A98 P27-A81 P27-A83 P28-A127 P29-A163 P3-A33 P3-A4 P30-A64 P34-A174 P35-A55 P36-A128 P36-A92 P37-A137 P38-A100 P39-A63 P4-A34 P40-A106 P41-A107 P41-A27 P43-A196 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Décima iteração:
```shell
Iteração 10
Inserindo o par : Projeto P10  Aluno A24
Inserindo o par : Projeto P28  Aluno A127
Inserindo o par : Projeto P27  Aluno A83
Inserindo o par : Projeto P30  Aluno A64
Inserindo o par : Projeto P18  Aluno A22
Inserindo o par : Projeto P49  Aluno A199
Inserindo o par : Projeto P43  Aluno A196
Inserindo o par : Projeto P25  Aluno A84
Inserindo o par : Projeto P36  Aluno A56
Inserindo o par : Projeto P41  Aluno A97
Inserindo o par : Projeto P37  Aluno A177
Inserindo o par : Projeto P38  Aluno A62
Inserindo o par : Projeto P24  Aluno A91
Inserindo o par : Projeto P48  Aluno A85
Inserindo o par : Projeto P26  Aluno A48
Inserindo o par : Projeto P26  Aluno A143
Inserindo o par : Projeto P8  Aluno A188
Inserindo o par : Projeto P55  Aluno A26
Inserindo o par : Projeto P34  Aluno A174
Inserindo o par : Projeto P3  Aluno A4
Inserindo o par : Projeto P8  Aluno A18
Inserindo o par : Projeto P36  Aluno A68
Inserindo o par : Projeto P21  Aluno A147
Inserindo o par : Projeto P44  Aluno A82
Inserindo o par : Projeto P45  Aluno A155
Inserindo o par : Projeto P6  Aluno A8
Inserindo o par : Projeto P12  Aluno A31
Inserindo o par : Projeto P7  Aluno A187
Inserindo o par : Projeto P51  Aluno A96
Inserindo o par : Projeto P2  Aluno A32
Inserindo o par : Projeto P41  Aluno A27
Inserindo o par : Projeto P4  Aluno A34
Inserindo o par : Projeto P27  Aluno A81
Inserindo o par : Projeto P40  Aluno A6
Inserindo o par : Projeto P53  Aluno A95
Inserindo o par : Projeto P9  Aluno A66
Inserindo o par : Projeto P16  Aluno A42
Inserindo o par : Projeto P7  Aluno A117
Inserindo o par : Projeto P14  Aluno A93
Inserindo o par : Projeto P1  Aluno A2
Inserindo o par : Projeto P35  Aluno A55
Inserindo o par : Projeto P15  Aluno A135
Inserindo o par : Projeto P9  Aluno A23
Inserindo o par : Projeto P17  Aluno A61
Inserindo o par : Projeto P53  Aluno A60
Inserindo o par : Projeto P3  Aluno A33
Inserindo o par : Projeto P14  Aluno A41
Inserindo o par : Projeto P39  Aluno A63
Inserindo o par : Projeto P47  Aluno A158
Inserindo o par : Projeto P23  Aluno A197
Inserindo o par : Projeto P5  Aluno A35
Inserindo o par : Projeto P15  Aluno A14
Retirando o par: Projeto P41 Aluno A97
Inserindo o par : Projeto P41  Aluno A107
Inserindo o par : Projeto P5  Aluno A185
Inserindo o par : Projeto P22  Aluno A144
Inserindo o par : Projeto P50  Aluno A1
Inserindo o par : Projeto P1  Aluno A200
Inserindo o par : Projeto P29  Aluno A163
Inserindo o par : Projeto P20  Aluno A72
Retirando o par: Projeto P21 Aluno A147
Inserindo o par : Projeto P21  Aluno A137
Retirando o par: Projeto P41 Aluno A27
Inserindo o par : Projeto P41  Aluno A107
Retirando o par: Projeto P3 Aluno A4
Inserindo o par : Projeto P3  Aluno A100
Retirando o par: Projeto P18 Aluno A22
Inserindo o par : Projeto P18  Aluno A157
Retirando o par: Projeto P20 Aluno A72
Inserindo o par : Projeto P20  Aluno A100
57 pares: P1-A2 P1-A200 P10-A24 P12-A31 P14-A41 P14-A93 P15-A135 P15-A14 P16-A42 P17-A61 P18-A157 P2-A32 P20-A100 P21-A137 P22-A144 P23-A197 P24-A91 P25-A84 P26-A143 P26-A48 P27-A81 P27-A83 P28-A127 P29-A163 P3-A100 P3-A33 P30-A64 P34-A174 P35-A55 P36-A56 P36-A68 P37-A177 P38-A62 P39-A63 P4-A34 P40-A6 P41-A107 P43-A196 P44-A82 P45-A155 P47-A158 P48-A85 P49-A199 P5-A185 P5-A35 P50-A1 P51-A96 P53-A60 P53-A95 P55-A26 P6-A8 P7-A117 P7-A187 P8-A18 P8-A188 P9-A23 P9-A66
```
### Maior emparelhamento obitdo:
```shell
MAIOR PAREAMENTO ENCONTRADO
Tamanho : 58
P1 A2
P1 A200
P10 A24
P12 A31
P14 A41
P14 A93
P15 A135
P15 A14
P16 A42
P17 A161
P18 A177
P2 A32
P20 A64
P21 A157
P22 A144
P23 A197
P24 A114
P25 A84
P26 A142
P26 A98
P27 A81
P27 A83
P28 A127
P29 A163
P3 A100
P3 A33
P30 A64
P34 A174
P35 A175
P36 A56
P36 A92
P37 A61
P38 A62
P39 A63
P4 A34
P40 A84
P41 A107
P41 A197
P43 A153
P44 A82
P45 A155
P47 A158
P48 A85
P49 A199
P5 A35
P5 A85
P50 A1
P51 A96
P53 A60
P53 A95
P55 A26
P6 A8
P7 A117
P7 A187
P8 A18
P8 A188
P9 A23
P9 A66
```
