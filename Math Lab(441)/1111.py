import numpy as np

def check_consistency(A, B):
    augmented = np.hstack((A, B))
    rank_A = np.linalg.matrix_rank(A)
    rank_aug = np.linalg.matrix_rank(augmented)
    variables = A.shape[1]

    if rank_A != rank_aug:
        return "Inconsistent system (No solution)"
    elif rank_A == variables:
        return "Consistent system with UNIQUE solution"
    else:
        return "Consistent system with INFINITELY MANY solutions"
A = np.array([[1,1,1],[2,2,2],[3,3,3]])
B = np.array([[6],[12],[18]])
print(check_consistency(A, B))


