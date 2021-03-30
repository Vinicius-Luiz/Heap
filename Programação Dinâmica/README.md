### Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
### Centro de Informática (CIn) (http://www.cin.ufpe.br)
### Graduando em Sistemas de Informação
### IF969 - Algoritmos e Estrutura de Dados

### Autor: Vinícius Luiz da Silva França (vlsf2)
### Email: vlsf2@cin.ufpe.br
### Data: 2020-11-22

### Copyright(c) 2020 Vinícius Luiz da Silva França


##### A contratação de jogadores em clubes de futebol pode ser uma tarefa bastante complicada, com preços de transferências que chegam a ultrapassar milhões de euros.
##### Consequentemente, os clubes esperam um bom retorno dos jogadores contratados, fazendo com que o time alcance seus objetivos da maneira mais eficiente possível.
##### Para este problema, um clube de futebol contratou um time de especialistas para avaliar uma lista de jogadores que podem ser contratados, dando a cada um dos jogadores uma pontuação. Quanto maior a pontuação de uma jogador, melhor é a contratação dele para o clube.
##### Apesar de querer contratar os jogadores com maiores pontuações, o clube possui uma certa quantia de dinheiro disponível para a contratação de novos jogadores. Desta forma, você deverá encontrar a melhor combinação de contratação possível.
##### A melhor combinação de contratação possível tem o foco em obter a maior soma de pontuações com o menor custo, não importando a quantidade de jogadores contratados, ou seja, é melhor contratar um jogador de pontuação 9 do que 2 jogadores que juntos somam uma pontuação de 8.

> Ex:
Jogador A com preço 10 e pontuação 9
Jogador B com preço 7 e pontuação 6
Jogador C com preço 4 e pontuação 4
Jogador D com preço 15 e pontuação 20

Se o clube tem 11 milhões de euros disponíveis, seria melhor contratar os jogadores B e C com pontuação total de 10 (6+4), gastando 11 milhões.
Se o clube tem 10 milhões de euros disponíveis, seria melhor contratar o jogador A com pontuação total de 9, gastando 10 milhões.
Se o clube tem 18 milhões de euros disponíveis, seria melhor contratar o jogador D com pontuação 20, gastando 15 milhões.

> Input Specification
D - A primeira entrada possui um inteiro D que corresponde à quantidade de dinheiro disponível para contratações.
N - A segunda entrada possui um inteiro N que representa a quantidade de jogadores disponíveis para contratação Em seguida, seguem N entradas no formato:
n;c;p -> Onde n é o nome do jogador, c é o seu custo de transferência em milhões de euros e p é a sua pontuação.

> Output Specification
A primeira saída deve corresponder à soma das pontuações dos jogadores que formam a melhor combinação de contratação possível;	
A segunda linha deve conter o dinheiro gasto com esta combinação;
Em seguida, em cada linha, devem ser impressos os nomes dos jogadores que formam esta contratação. (Na ordem em que aparecem no input)