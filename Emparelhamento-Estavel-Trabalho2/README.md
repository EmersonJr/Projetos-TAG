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

O problema proposto consiste em encontrar um emparelhamento estável e máximo para a atribuição de alunos a projetos. Cada aluno recebe uma nota, calculada com base em seu histórico e tempo disponível. Além disso, os alunos apresentam uma lista com até três projetos, ordenada por ordem de preferência, aos quais têm interesse em se vincular. Para os projetos, são especificadas a nota mínima exigida e a capacidade máxima de participantes. Os responsáveis pelos projetos buscam selecionar os alunos com as maiores notas, priorizando, portanto, aqueles que apresentam melhor desempenho nas métricas definidas.
