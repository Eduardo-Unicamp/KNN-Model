from knn import euclidean_distance,knn, dataset_knn, file_dataset_knn
from data import data,no_class
from efficiency_test import efficiency_test
from best_k_tester import best_k_finder


print(knn(data,(5700., 2900., 4200., 1300.),k=5)) #RETORNA a classificação de um ponto com base em uma base de dados e um valor de k

dataset_knn(data,no_class)# executa a função knn para cada valor de uma base de analise dada, e RETORNA E EXIBE uma lista com as CPF, classificação e coordenadas do ponto

file_dataset_knn(data,no_class)#RETORNA E EXIBE os mesmos dados da função knn, porém criando um arquivo .txt no diretorio local
