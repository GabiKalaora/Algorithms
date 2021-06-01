def kanpsack(W, weight, values):
     # init table of size num_of_items x W
    table = [[0 for i in range(W + 1)] for j in range(len(values) + 1)]
    
    for i in range(len(values) + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weight[i - 1] <= j:
                table[i][j] = max(values[i - 1] + table[i - 1][j - weight[i - 1]], 
                                  table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    return table[len(values)][W]






print(kanpsack(5, [4, 2, 2], [150, 100, 100]))