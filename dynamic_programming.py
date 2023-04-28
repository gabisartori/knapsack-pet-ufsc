# esse código pretende resolver o problema da mochila (knapsack problem) com programação dinâmica
import time

def knapsack(W, wt, val, n):
    inicio = time.time()
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0: # caso base
                K[i][w] = 0
            elif wt[i-1] <= w: # se o peso do item é menor ou igual ao peso da mochila
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]) # pega o maior valor entre colocar o item na mochila e não colocar
            else: # se o peso do item é maior que o peso da mochila
                K[i][w] = K[i-1][w] # não coloca o item na mochila
    fim = time.time()
    tempo = fim - inicio
    return [K[n][W], tempo]

# w = peso da mochila
# wt = vetor com os pesos dos itens
# val = vetor com os valores dos itens
# n = número de itens

r = knapsack(180, [10, 20, 30, 50, 65, 70, 80, 95], [60, 100, 120, 140, 700, 800, 850, 855], 8)
print(r[0])
print("Tempo de execução: {} ms".format(r[1]*10**3))


