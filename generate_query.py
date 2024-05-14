import numpy as np 

n = 1000
d = 100
c = 5
ep = 3
eta = d + 1 + c + ep


data_to_save = np.random.randint(0,10, size=d)

# Save data to a CSV file
np.savetxt('query_user/query_og.csv', data_to_save, delimiter=',')