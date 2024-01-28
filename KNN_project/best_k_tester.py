from efficiency_test import efficiency_test,data
#algoritmo pra testar qual o melhor valor de k para a função

def best_k_finder(data:list,passed_k_limit = 20,k_list = []):
    k_limit = passed_k_limit
    best_value = 0
    efficiency_list = []
    rate = 0
    best_k = 0 
    if k_list == []:#se ele passa uma lista de k's, será feito o modo lista
        for i in range(1,k_limit+1):
            efficiency_list.append(efficiency_test(data,mode="use",k = i))
        rate = max(efficiency_list)
        best_k = efficiency_list.index(rate)+1
        print(best_k)
    else:
        for element in k_list:#se não passa uma lista, será feita para todos os valores até k_limit
            best_value = max(best_value,efficiency_test(data,mode="use",k = element))
        print(best_value)



best_k_finder(data)