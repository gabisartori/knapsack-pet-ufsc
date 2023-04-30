   # esse código pretende resolver o problema da mochila (knapsack problem) com programação dinâmica
import time
from random import randint
import numpy as np

def knapsack(p_max, p_items, value_items, n_items):
    inicio = time.time()
    K = np.zeros((n_items+1, p_max+1))
    for i in range(n_items+1):
        for p in range(p_max+1):
            if i == 0 or p == 0: # caso base
                K[i][p] = 0
            elif p_items[i-1] <= p_max and p_items[i-1] <= p: # se o peso do item é menor ou igual ao peso da mochila
                K[i][p] = max(K[i-1][p], value_items[i-1] + K[i-1][p-p_items[i-1]]) # pega o maior valor entre colocar o item na mochila e não colocar
            else: # se o peso do item é maior que o peso da mochila
                K[i][p] = K[i-1][p] # não coloca o item na mochila   

    utilidade = K[n_items][p_max]
    
    fim = time.time()
    tempo = fim - inicio

    print(K)
    return (utilidade, tempo)

print(knapsack(10, [5, 4, 6, 3], [10, 40, 30, 50], 4))

# O problema da mochila é classificado como NP-Completo, ou seja, não existe um algoritmo polinomial que resolva o problema.
# O algoritmo de programação dinâmica é um algoritmo pseudo-polinomial, ou seja, o tempo de execução do algoritmo é polinomial em relação ao peso da mochila, mas exponencial em relação ao número de itens.
# O algoritmo de força bruta é um algoritmo exponencial, ou seja, o tempo de execução do algoritmo é exponencial em relação ao peso da mochila e ao número de itens.
# O algoritmo de força bruta é mais eficiente que o algoritmo de programação dinâmica para valores pequenos de peso da mochila e número de itens, mas para valores grandes o algoritmo de programação dinâmica é mais eficiente.