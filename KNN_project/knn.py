


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


    #dar a resposta com base nisso
    conservador = 0
    moderado = 0
    agressivo = 0
    # ---- essa parte conta quantos são de cada categoria
    for pair in k_nearest_new:
        conservador += pair.count('Conservador')
        moderado += pair.count('Moderado')
        agressivo += pair.count('Agressivo')
    # ---- essa parte fala qual das categorias tem mais, já criando o resultado final da fução que será o deduction
        
    deduction = ''
    possibilities = {'Conservador': conservador,'Moderado':moderado,'Agressivo':agressivo}#nessa ordem pois em caso de empate optou-se por considerar a opçaõ mais agressiva
    if conservador == moderado and moderado == agressivo:
        deduction = k_nearest_new[0][0]#se houver mesmo numero de cada categoria, pega a categoria do ponto mais próximo
    else:
        for x in possibilities.values():
            if max(possibilities.values()) == x:
                deduction =list(possibilities.keys())[list(possibilities.values()).index(x)]
    
    #return
    return deduction




def dataset_knn(base_dataset:list,analysed_data:list):
    for sublist in analysed_data:
        sublist[1] = knn(base_dataset,sublist[2])
    print(analysed_data)
    return analysed_data
    

def file_dataset_knn(base_dataset:list,analysed_data:list):
    results_list = dataset_knn(base_dataset,analysed_data)
    written = False
    i = 1
    while  written == False:

        try:
            file = open(f'knn_output{i}.txt','x')
            file.close()
            file = open(f'knn_output{i}.txt','a+')
            file.write('Os resultados encontrados pelo modelo k-nearest neigbors para o conjunto apresentado foram:\n\n')
            for line in results_list:
                file.write(str(line))
                file.write('\n')  
            written = True
        except:
            i+=1
  
    file.close()