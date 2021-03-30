class Heap:
    def __init__(self, comprimento):
        self.comprimento  = comprimento
        self.tamanho_heap = 0
        self.vetor        = []
        for i in range(self.comprimento):
            self.vetor.append(None)

    def pai(self, i):
        if i == 2:
            return 0
        else:
            return i//2

    def esquerda(self, i):
        return (2*i)+1

    def direita(self,i):
        return (2*i)+2

    def heap_inserir(self, chave):
        vetor = self.vetor
        vetor[self.tamanho_heap] = -1
        self.heap_incrementar(self.tamanho_heap, chave)
        self.tamanho_heap += 1

    def heap_incrementar(self, i, chave):
        vetor = self.vetor
        if chave < vetor[i]:
            return
        vetor[i] = chave
        fim = False
        if vetor[self.pai(i)] is None:
            vetor[i], vetor[self.pai(i)] = vetor[self.pai(i)], vetor[i]
            return
        while not fim and vetor[self.pai(i)] > vetor[i]:
            vetor[i], vetor[self.pai(i)] = vetor[self.pai(i)], vetor[i]
            if i > 0:
                i = self.pai(i)
            else:
                fim = True

    def min_heapify(self, i = 0):
        menor    = i
        esquerda = self.esquerda(i)
        direita  = self.direita(i)
        vetor    = self.vetor
        if esquerda < self.tamanho_heap and vetor[esquerda] < vetor[i]:
            menor = esquerda
            
        if direita < self.tamanho_heap and vetor[direita] < vetor[menor]:
            menor = direita

        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            self.min_heapify(menor)
        else:
            if menor+1 <= self.comprimento:
                self.min_heapify(menor+1)

    def heap_min_remover(self):
        vetor = self.vetor
        if vetor[0] is None:
            return
        if self.tamanho_heap == 1:
            vetor[0] = None
            return
        else:
            vetor[0], vetor[-1] = vetor[-1], vetor[0]
            self.tamanho_heap -= 1
            return self.min_heapify()

    def max_heapify(self, i = 0):
        maior = i
        esquerda = self.esquerda(i)
        direita  = self.direita(i)
        vetor = self.vetor
        if esquerda < self.tamanho_heap and vetor[esquerda] > vetor[i]:
            maior = esquerda

        if direita < self.tamanho_heap and vetor[direita] > vetor[maior]:
            maior = direita

        if maior != i:
            vetor[i], vetor[maior] = vetor[maior], vetor[i]
            self.max_heapify(maior)
        else:
            if maior+1 <= self.comprimento:
                self.max_heapify(maior+1)

    def heap_max_remover(self):
        self.max_heapify()
        vetor = self.vetor
        if vetor[0] is None:
            return
        if self.tamanho_heap == 1:
            vetor[0] = None
            return
        else:
            vetor[0], vetor[-1] = vetor[-1], None
            self.tamanho_heap -= 1
            return self.max_heapify()

    def heap_imprimir(self):
        return self.vetor

class Heapsort(Heap):
    def __init__(self, vetor):
        self.vetor        = vetor
        self.comprimento  = len(self.vetor)
        self.tamanho_heap = self.comprimento
        self.build_max_heap(self.vetor)

    def build_max_heap(self, vetor):
        for i in range(((self.comprimento)//2)-1, -1, -1):
            self.max_heapify(i)

    def ordenar_heap(self):
        vetor = self.vetor
        self.build_max_heap(vetor)
        for i in range(self.comprimento-1, 1, -1):
            temp = vetor[0]
            vetor[0] = vetor[i]
            vetor[i] = temp
            self.altura_heap -= 1
            self.max_heapify(0)
    
    def heap_extract_max(self):
        vetor = self.vetor
        if self.tamanho_heap <1:
            return 'Heap underflow'
        maior = vetor[0]
        vetor[0] = vetor[self.tamanho_heap]
        self.tamanho_heap -= 1
        self.max_heapify(0)
        return maior

    def heap_imprimir(self):
        return self.vetor
            

#tam = int(input('comprimento do vetor: '))
#h = Heap(tam)
h = Heap(5)
h.heap_inserir(10)
h.heap_inserir(5)
h.heap_inserir(8)
h.heap_inserir(2)
h.heap_inserir(4)
h.max_heapify()
print(h.heap_imprimir())
h.min_heapify()
print(h.heap_imprimir())



