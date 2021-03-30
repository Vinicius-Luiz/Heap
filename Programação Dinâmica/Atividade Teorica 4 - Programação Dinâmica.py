def main():
    def melhorCombo(tJ, tC, j):
        matriz = [[0]*(tC+1)]
        for i in range(tJ):
            linhaTemp = [0]*(tC+1)
            matriz.append(linhaTemp)
        iLinha = 1
        while iLinha <= tJ:
            iColuna = 0
            for coluna in matriz[iLinha]:
                if iColuna >= j[iLinha][1]:
                    v1 = matriz[iLinha-1][iColuna]
                    v2 = j[iLinha][2] + matriz[iLinha-1][iColuna - j[iLinha][1]] 
                    matriz[iLinha][iColuna] = max(v1, v2)
                else:
                    matriz[iLinha][iColuna] = matriz[iLinha-1][iColuna]
                iColuna += 1
            iLinha += 1
        #for i in range (1, len(matriz)):
         #   print(matriz[i])#, j[i][0])

        melhorPontuacao = 0
        melhorValor = 0
        melhoresJogadores = []
        iColunaTemp = -1
        for linha in range(tJ, 0, -1):
             if matriz[linha][iColunaTemp] != matriz[linha-1][iColunaTemp]:
                 melhoresJogadores.append(j[linha][0])
                 melhorValor += j[linha][1]
                 melhorPontuacao += j[linha][2]
                 iColunaTemp -= j[linha][1]

        print(melhorPontuacao)
        print(melhorValor)
        for i in range(len(melhoresJogadores)-1, -1, -1):
            print(melhoresJogadores[i])

    totalCaixa     = int(input())
    totalJogadores = int(input())
    jogadores      = {}
    for i in range(1, totalJogadores+1):
        jogador = input()
        jogador = jogador.split(';')
        jogador = (jogador[0], int(jogador[1]), int(jogador[2]))
        jogadores[i] = jogador

    melhorCombo(totalJogadores, totalCaixa, jogadores)

if __name__ == '__main__':
    main()
