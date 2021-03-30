def main():
    def melhorCombo(qtd_jogadores, valor_total, jogadores):
        #criando uma matriz:
        #quantidade de linhas: quantidade de jogadores + 1
        #quantidade de colunas: valor total pra se gastar + 1
        matriz = [[0]*(valor_total+1)]
        for i in range(qtd_jogadores):
            linha = [0]*(valor_total+1)
            matriz.append(linhaTemp)

        
        iLinha = 1
        while iLinha <= qtd_jogadores:
            #o while vai rodar a linha de todos os jogadores a partir do indice 1
            #não se começa pelo indice 0 porque a linha 0 equivale a 'nenhum jogador'
            iColuna = 0
            #acho q a iColuna pode começar a partir do indice 1 tb, testa dps
            for coluna in matriz[iLinha]:
                if iColuna >= jogadores[iLinha][1]:
                    #se iColuna (valor que pode ser gasto) for maior ou igual ao preço do jogador, entra aqui
                    #exemplo, se eu posso gastar 7$ e o valor do jogador é 5$, então entra
                    v1 = matriz[iLinha-1][iColuna]
                    v2 = jogadores[iLinha][2] + matriz[iLinha-1][iColuna - jogadores[iLinha][1]] 
                    matriz[iLinha][iColuna] = max(v1, v2)
                    #a gente ver qual é o maior valor entre v1 e v2
                    #v1 = valor que está na msm coluna, mas uma linha acima
                    #v2 = pontuacao do jogador + pontuacao salva na linha anterior e na coluna N - valor do jogador
                else:
                    #se não entrar no if acima, ele repete o valor da linha acima da msm coluna
                    matriz[iLinha][iColuna] = matriz[iLinha-1][iColuna]
                iColuna += 1
            iLinha += 1

        #se quiser printar a matriz p ver como fica, ta ai, mas tem que apagar p entregar no iudex    
        for i in range (1, len(matriz)):
            print(matriz[i], jogadores[i][0])

        melhorPontuacao = 0 #melhor pontuacao tb pode ser 'matriz[-1][-1]' dai n precisa calcular ele no for abaixo
        melhorValor = 0
        melhoresJogadores = []
        iColunaTemp = -1
        for linha in range(qtd_jogadores, 0, -1):
            #esse for vai rodar de baixo pra cima, do ultimo indice até o primeiro
             if matriz[linha][iColunaTemp] != matriz[linha-1][iColunaTemp]:
                 #se o valor q está na linha X coluna Y for diferente do valor que está na linha X-1 e coluna Y
                 #significa que o jogador da linha X foi usado
                 melhoresJogadores.append(jogadores[linha][0]) #adiciono o nome do jogador na lista
                 melhorValor += jogadores[linha][1] #adiciono o valor do jogador adicionado
                 melhorPontuacao += jogadores[linha][2] #se tu seguira a dica que dei do [matriz][-1][-1] tu pode apagar isso
                 iColunaTemp -= jogadores[linha][1] #se eu to na coluna X, eu vou pra coluna X - valor do jogador adicionado

        print(melhorPontuacao)
        print(melhorValor)
        for i in range(len(melhoresJogadores)-1, -1, -1):
            #printar os melhores jogadores de forma inversa
            print(melhoresJogadores[i])

    valor_total     = int(input()) #quanto se pode gastar
    qtd_jogadores = int(input())
    jogadores      = {}
    for x in range(1, totalJogadores+1):
        #cada jogador eu coloco num dicionário, onde a chave é a ordem de 'chegada'
        #exemplo
        #o primeiro input é ronaldo, então a chave de ronaldo é 1 e os valores é o nome dele, valor e pontuacao
        #o segundo input é ney, entao a chave de ney e 2 e os valores...
        jogador = input()
        jogador = jogador.split(';')
        jogador[1], jogador[2] = int(jogador[1]), int(jogador[2])
        jogadores[i] = jogador

    programacaoDinamica(qtd_jogadores, valor_total, jogadores)

if __name__ == '__main__':
    main()
