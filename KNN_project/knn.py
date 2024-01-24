points = {'categoryA' : [[1,2],[1,4],[3,2],[4,2],[3,4],], 'categoryB': [[10,20],[11,22],[14,10],[21,22],[21,19]]}#pontos iniciais


def euclidean_distance(dimensions:int, initial_point_coordinates:list,final_point_coordinates:list):
    initial = initial_point_coordinates
    final = final_point_coordinates
    n = dimensions
    sum = 0

    for i in range(n):
        sum += (final[i]-initial[i])**2
    
    distance = sum**(1/2)
    return distance





def knn(dimensions,*coordinates, initial_points = points):#recebe o numero de dimensões e as coordenadas, esse poinsts por padrão pode tirar depois
    pass

    
