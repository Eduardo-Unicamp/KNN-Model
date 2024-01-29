from efficiency_test import efficiency_test
from data import data

#algoritmo pra testar qual o melhor valor de k para a função

def best_k_finder(data:list,passed_k_limit = 20):
    k_limit = passed_k_limit
    best_value = 0
    efficiency_list = []
    rate = 0
    best_k = 0 

    for i in range(1,k_limit+1):
        efficiency_list.append(efficiency_test(data,mode="use",k = i))
    rate = max(efficiency_list)
    best_k = efficiency_list.index(rate)+1
    print(best_k)
   

best_k_finder(data)