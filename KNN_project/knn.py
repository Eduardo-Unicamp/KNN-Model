


def euclidean_distance(dimensions:int, initial_point_coordinates:list,final_point_coordinates:list):
    initial = initial_point_coordinates
    final = final_point_coordinates
    n = dimensions
    sum = 0

    for i in range(n):
        sum += (final[i]-initial[i])**2
    
    distance = sum**(1/2)
    return distance





def knn(data:list,analysed_point_coordinates:tuple):
    distances_list = []
    
    #calcular todas as distancias
    for client in data:
        values_tuple = client[2]
        distances_list.append(euclidean_distance(len(values_tuple),list(values_tuple),list(analysed_point_coordinates)))
        
    print(distances_list)



    #ver quais as k menores


    
    #dar a resposta com base nisso
    
