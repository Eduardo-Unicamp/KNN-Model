


def euclidean_distance(dimensions:int, initial_point_coordinates:list,final_point_coordinates:list):
    initial = initial_point_coordinates
    final = final_point_coordinates
    n = dimensions
    sum = 0

    for i in range(n):
        sum += (final[i]-initial[i])**2
    
    distance = sum**(1/2)
    return distance





def knn(data:list,analysed_point_coordinates:tuple, k = 3):
    distances_dict = {}
    
    #calcular todas as distancias
    for client in data:
        values_tuple = client[2]
        distances_dict.update({client[0]:euclidean_distance(len(values_tuple),list(values_tuple),list(analysed_point_coordinates))})
        
    #ver quais as k menores
    sorted_list = sorted(distances_dict.items(),key=lambda x:x[1])
    k_nearest = sorted_list[0:k]

    #descobrir a categoria de cada cpf de k_nearest : já que como o dict nao aceita chave repetida tem identificar a distancia 
    #pelo cpf primeiro(o qual nao repete) e só depois ver qual o perfil daquele cpf
    category = ''
    k_nearest_new = []

    for cpf_distance in k_nearest:
        cpf = cpf_distance[0]
        distance = cpf_distance[1]

        for client in data:
            if cpf in client:
                category = client[1]
                k_nearest_new.append([category,distance])
    print(k_nearest_new)
        




    #print(distances_dict,'\n\n',sorted_list,'\n\n',k_nearest,'\n\n')


    #dar a resposta com base nisso
    
    #---------------COMMENT TO AVOID GETTING LOOSSSSSSSTTT IN CTRL-Z -------------------------------------------------------------#