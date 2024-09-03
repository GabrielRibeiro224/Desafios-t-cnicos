int Indice = 13, 
SOMA = 0, 
K = 0;

While K < Indice do {
    K = K + 1;
    SOMA = SOMA + K;
}

imprimir(SOMA);

// O valor da variável `Soma` é 91

// Explicação do código

/* 
INDICE = 13

SOMA = 0 

K = 0

Laço de repetição 

O laço `While(ENQUANTO) K < INDICE` vai executar enquanto o `K` for menor que `INDICE`

Em cada iteração:

`K` é incrementado em 1 (`K = K + 1`)
`SOMA` recebe o valor de `SOMA + K`


1ª iteração: K = 1, SOMA = 0 + 1 = 1
2ª iteração: K = 2, SOMA = 1 + 2 = 3
3ª iteração: K = 3, SOMA = 3 + 3 = 6
4ª iteração: K = 4, SOMA = 6 + 4 = 10
5ª iteração: K = 5, SOMA = 10 + 5 = 15
6ª iteração: K = 6, SOMA = 15 + 6 = 21
7ª iteração: K = 7, SOMA = 21 + 7 = 28
8ª iteração: K = 8, SOMA = 28 + 8 = 36
9ª iteração: K = 9, SOMA = 36 + 9 = 45
10ª iteração: K = 10, SOMA = 45 + 10 = 55
11ª iteração: K = 11, SOMA = 55 + 11 = 66
12ª iteração: K = 12, SOMA = 66 + 12 = 78
13ª iteração: K = 13, SOMA = 78 + 13 = 91
*/