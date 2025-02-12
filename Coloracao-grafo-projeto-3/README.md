# Trabalho 3 - Coloração de grafo

<h2>⌨️ Autores</h2>
<ul>
  <li>Iasmim de Queiroz Freitas - 190108665</li>
  <li>Emerson Luiz Cruz Junior - 231003531</li>
</ul>
<table>
  <tr>
    <td align="center"><a href="https://github.com/iasmimqf" target="_blank"><img style="border-radius: 50%;" src="https://github.com/iasmimqf.png" width="100px;" alt="Iasmim"/><br /><sub><b>Iasmim</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/EmersonJr" target="_blank"><img style="border-radius: 50%;" src="https://github.com/EmersonJr.png" width="100px;" alt="Emerson Junior"/><br /><sub><b>Emerson Junior</b></sub></a><br /></td>
</table>

# Setup

É necessário ter o compilador python instalado e o gerenciador de pacots `pip` para instalar as bibliotecas que nos auxiliaram na implementação desse trabalho.

```shell
pip install matplotlib networkx
```

# Run

Execute um dos comandos abaixo para executar o programa:


```shell
py main.py
```

ou


```shell
python main.py
```

# O problema:

O projeto consistia em encontrar uma disposição de partidas para um campeonato com sete times definido pelo seguinte formato:

- 14 partidas devem acontecer
- Todos os times jogam duas vezes entre si, uma vez como mandante e a outra como visitante

Por conta, de problemas comerciais ou de segurança algumas partidas devem acontecer obrigatoriamente em rodadas diferentes.

A tabela a seguir apresenta os times participantes do campeonato, bem como as restrições para a disposição dos jogos:

<img alt="tabela" src="./tabela_campeonato.png" />
