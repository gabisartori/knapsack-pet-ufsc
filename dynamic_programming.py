# esse código pretende resolver o problema da mochila (knapsack problem) com programação dinâmica
import time
from random import randint

def knapsack(p_max, p_items, value_items, n_items):
    inicio = time.time()
    K = [[0 for x in range(p_max+1)] for x in range(n_items+1)]
    for i in range(n_items+1):
        for p in range(p_max+1):
            if i == 0 or p == 0: # caso base
                K[i][p] = 0
            elif p_items[i-1] <= p_max: # se o peso do item é menor ou igual ao peso da mochila
                K[i][p] = max(value_items[i-1] + K[i-1][p_max-p_items[i-1]], K[i-1][p_max]) # pega o maior valor entre colocar o item na mochila e não colocar
            else: # se o peso do item é maior que o peso da mochila
                K[i][p] = K[i-1][p] # não coloca o item na mochila
    fim = time.time()
    tempo = fim - inicio
    utilidade = K[n_items][p_max]
    return (utilidade, tempo)

n = 100


r = knapsack(400, [randint(20, 600) for i in range(n)], [randint(900, 3000) for i in range(n)], n)
print(r[0])
print("Tempo de execução: {} seg".format(r[1]))