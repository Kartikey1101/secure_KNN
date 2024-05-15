import numpy as np 

n = 100
d = 100
c = 5
ep = 3
eta = d + 1 + c + ep

data_to_save = np.random.randint(0,10000, size=(n, d))

# Save data to a CSV file
np.savetxt('data_user/data_og.csv', data_to_save, delimiter=',')