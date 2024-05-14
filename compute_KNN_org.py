import numpy as np
import os
from sklearn.neighbors import NearestNeighbors

orignal_data = np.loadtxt('data_user/data_og.csv', delimiter=',')
q_0 = np.loadtxt('query_user/query_og.csv', delimiter=',').reshape(1, -1)

k = 10      # Number of nearest neighbors to find


def find_k_nearest_neighbors(data_matrix, q_0, k):
    # Using sklearn's NearestNeighbors for efficiency
    nbrs = NearestNeighbors(n_neighbors=k, algorithm='auto').fit(data_matrix)
    distances, indices = nbrs.kneighbors(q_0)
    return distances, indices




distances, indices = find_k_nearest_neighbors(orignal_data, q_0, k)
print("\nIndices of the nearest neighbors for each query point:")
np.savetxt('data_val/knn_og.csv', indices, delimiter=',')
print(indices)