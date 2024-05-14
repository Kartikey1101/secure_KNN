import numpy as np
import os

indices_og = (np.sort(np.loadtxt('data_val/knn_og.csv', delimiter=','))).astype(int)
indices_cal = np.sort(np.loadtxt('query_user/knnResult.csv', delimiter=',')).astype(int)
original_query = np.sort(np.loadtxt('query_user/query_og.csv', delimiter=',')).astype(int)
original_data = np.loadtxt('data_user/data_og.csv', delimiter=',')
mask = np.isin(indices_cal, indices_og)

# Delete similar elements from indices_cal
indices_cal_unique = indices_cal[~mask]

# Delete similar elements from indices_og
indices_og_unique = indices_og[~mask]
n = len(indices_og_unique)
m = len(indices_cal)
mse=0
distance_og = np.ones(m)
distance_enc = np.ones(m)
for i in range(m):
    distance_og[i] = np.linalg.norm(original_data[indices_og[i]]- original_query)
    distance_enc[i] = np.linalg.norm(original_data[indices_cal[i]] - original_query)

for i in range(n):
    mse+= np.linalg.norm(original_data[indices_cal_unique[i]]-original_data[indices_og_unique[i]])
    
print((mse))
# print(np.sort(distance_og))
# print(np.sort(distance_enc))