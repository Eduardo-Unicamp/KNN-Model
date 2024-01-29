from knn import euclidean_distance, knn, dataset_knn, file_dataset_knn
from data import data, no_class


def efficiency_test(data:list,mode ="see",k = 3):
    #define para cada elemento se houve acerto ou erro
    right_answer_list = []
    for client in data:
        client_data = client
        new_data = data.copy()
        new_data.remove(client_data)
        result = knn(new_data,client_data[2],k = k)
        if result == client_data[1]:
            right_answer_list.append('acerto')
        else:
            right_answer_list.append('erro')
    #conta a quantidade de erros e acertos
        acertos = right_answer_list.count('acerto')
        erros = right_answer_list.count('erro')
    #calcula a porcentagem de acertos
        accuracy = acertos*100/120
    #return
    if mode == "see":#use este modo para ver a acuracia diretamente e formatada 
        return f'acurária:{accuracy:.1f}%'
    elif mode =="list":#use este modo para listar todos os erros e acertos (debug)
        return right_answer_list, f'acurária:{accuracy:.1f}%'
    elif mode == "use":
        return accuracy#use este modo para receber só o resultado da acuracia e usar em alguma outra função


