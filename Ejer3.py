import numpy as np

def TwoOpt(perm):
    n = perm.shape[0]
    neighbors = []
    for i in range(n-1):
        for j in range(i+2, n):
            if not (i == 0 and j == n-1):
                new_perm = perm.copy()
                new_perm[i:j+1] = perm[i:j+1][::-1] 
                neighbors.append(new_perm)
    return np.array(neighbors)

perm = np.array([0, 1, 2, 3, 4, 5])
neighbors = TwoOpt(perm)
print(neighbors)
