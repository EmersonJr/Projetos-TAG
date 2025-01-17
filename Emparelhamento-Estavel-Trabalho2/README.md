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

Seguindo os requisitos do trabalho, o algoritmo é rodado 10 vezes , buscando atingir o melhor emparelhamento possível, alterando a ordem em que os alunos são colocados na fila em cada iteração.

A resposta final é obtida considerando o maior emparelhamento encontrado durante as 10 iterações .

