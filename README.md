<h1>Problema das 8 Rainhas - Solução em Python</h1>
<img src="https://img.shields.io/badge/Python-3.8%252B-blue">
<img src="https://img.shields.io/badge/status-complete-brightgreen">

Uma implementação completa do clássico Problema das 8 Rainhas utilizando o algoritmo de Backtracking em Python.

<h2>👥 Autores</h2>
Andreza Falcão<br>
Eduardo Sampaio<br>
Paloma Santos

<h2>📋 Sobre o Problema</h2>
O Problema das 8 Rainhas é um desafio clássico da ciência da computação e matemática que consiste em colocar 8 rainhas em um tabuleiro de xadrez 8×8 de forma que nenhuma rainha ataque outra.

<h2>🎯 Regras do Jogo</h2>

Uma rainha pode mover-se qualquer número de casas em linha reta:

Horizontalmente (mesma linha)

Verticalmente (mesma coluna)

Diagonalmente (ambas as diagonais)

Objetivo: Posicionar 8 rainhas de modo que nenhuma esteja na linha, coluna ou diagonal de outra

<h2>🔢 Fatos Interessantes</h2>

Existem 92 soluções distintas para o problema

Considerando simetrias (rotações e reflexões), existem 12 soluções fundamentalmente diferentes

O problema pode ser generalizado para N rainhas em um tabuleiro N×N

<h2>🚀 Funcionalidades</h2>

✅ Backtracking completo: Encontra todas as 92 soluções

🎨 Visualização gráfica: Exibe o tabuleiro com formatação no terminal

📊 Estatísticas: Mostra informações sobre distribuição das soluções

🔍 Seleção por índice: Visualiza qualquer uma das 92 soluções

📱 Interface de menu: Navegação intuitiva via terminal

<h2>🛠️ Tecnologias Utilizadas</h2>

Python 3.8+

Algoritmo de Backtracking

Manipulação de matrizes bidimensionais

Formatação de saída em terminal

<h2>🖥️ Interface do Programa</h2>
Ao executar, você verá um menu com as seguintes opções:

Tempo para encontrar todas as soluções: 0.0452 segundos
Total de soluções encontradas: 92

Opções:
1. Ver todas as soluções (formato compacto)
2. Visualizar uma solução específica
3. Ver estatísticas
4. Sair

<h2>📊 Exemplo de Saída</h2>
Visualização de uma solução:<br>
Texto 0 1 2 3 4 5 6 7<br>
  ----------------<br>
0|. . . Q . . . . <br>
1|. . . . . . Q . <br>
2|. . Q . . . . . <br>
3|. . . . . . . Q <br>
4|. Q . . . . . . <br>
5|. . . . Q . . . <br>
6|Q . . . . . . . <br>
7|. . . . . Q . . 

<h2>⚙️ Implementação Técnica</h2>

<h3>Algoritmo de Backtracking</h3>

O algoritmo funciona da seguinte forma:

Coloca uma rainha na primeira coluna

Move para a próxima coluna

Tenta colocar uma rainha em cada linha da coluna atual

Verifica segurança (linha, coluna e diagonais)

Se seguro, coloca a rainha e recursivamente tenta a próxima coluna

Se não encontrar posição segura, backtrack (volta à coluna anterior)

Repete até todas as rainhas estarem posicionadas

Complexidade
Tempo: O(N!) no pior caso

Espaço: O(N²) para armazenar o tabuleiro



