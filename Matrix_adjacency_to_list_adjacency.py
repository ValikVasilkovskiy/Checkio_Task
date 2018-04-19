def matrix_adjacency_to_list_adjacency(data):
    list_adjacency = []
    for i in list(zip(*data)):
        temp = []
        for j in range(len(i)):
            if i[j] == 1:
                temp.append(j)
        list_adjacency.append(temp)
    return list_adjacency
