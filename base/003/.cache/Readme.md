## @003 L1 - burn

![_](https://github.com/qxcodeed/arcade/blob/master/base/003/cover.jpg)

- Seja uma matriz de caracteres que representa um mapa de uma floresta.
- Cada caractere representa um espaço vazio ou uma árvore.
- O espaço vazio é representado por um ponto `.` e a árvore por uma hastag `#`.
- O fogo começa em um ponto inicial e se espalha para os vizinhos até que não haja mais árvores para queimar.

Dado a matriz da floresta e o ponto inicial onde começa o fogo, queime as árvores. O fogo se não se espalha nas diagonais, apenas nas 4 direções cardeais.

## Entrada

- 1a linha: `nl, nc, l, c`:
  - Número de linhas e colunas da matriz, linha e coluna onde começa o fogo.
- Nas linhas subsequentes a matriz da floresta sendo que
  - '\#' representa uma árvore
  - '.' representa um espaço vazio

## Saída

- A matriz após a queimada acontecer colocando 'o' para cada árvore queimada.

## Arquivos

- Você deve implementar:
  - [student.cpp](https://github.com/qxcodeed/arcade/blob/master/base/003/student.cpp)
    - escrever a função tocar_fogo.
- Já está implementado:
  - [main.cpp](https://github.com/qxcodeed/arcade/blob/master/base/003/main.cpp)
    - Faz a leitura da matriz e do ponto inicial
    - Chama a função tocar_fogo para o ponto inicial.
    - Imprime a matriz após a queimada.
  - [lib.hpp](https://github.com/qxcodeed/arcade/blob/master/base/003/lib.hpp)
    - Apenas o cabeçalho da função tocar_fogo.

## Testes

```txt
>>>>>>>> 01
2 3 1 1
#.#
.##
========
#.o
.oo
<<<<<<<<

>>>>>>>> 02
5 5 0 0
#..#.
#...#
###..
..#.#
..###
========
o..#.
o...#
ooo..
..o.o
..ooo
<<<<<<<<

>>>>>>>> 03
5 7 2 3
#..#.#.
#..####
####..#
..#.#..
#.###.#
========
o..o.o.
o..oooo
oooo..o
..o.o..
#.ooo.#
<<<<<<<<

```

## Ajuda

Você pode utilizar um vetor de strings para representar uma matriz de caracteres. Uma string é um vetor de caracteres. Dessa forma um `vector<string> mat` é uma vetor bidimensional. O exemplo a seguir já carrega a matriz na `main` e já faz um método capaz de imprimir a matriz. Você só precisa implementar o método `tocar_fogo`.

Utilize as seguintes regras para recursão.

- Se a posição for fora da matriz, retorne.
- Se a posição não for uma arvore retorne.
- Queime a arvore.
- Chame a recursão para todos os vizinhos.

