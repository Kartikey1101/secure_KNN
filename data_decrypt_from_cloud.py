import os
import numpy as np
m_base = np.loadtxt('data_user/secrets/m_base.csv', delimiter=',')
org_enc_data =  np.loadtxt('cloud/enc_data_cloud_1.csv', delimiter=',')

# print(org_enc_data)
# print(m_base)
d = 100 # need to be specified
multiplied = np.dot(org_enc_data,m_base)
# print(aa)

sec_vector =  np.loadtxt('data_user/secrets/sec_vector.csv', delimiter=',')
result_matrix = multiplied[:, :d]
sliced_sec_vector=sec_vector[:d]
# print(s)
final_decypted = 0.5 * ( sliced_sec_vector-result_matrix)
# print(final_decypted_csv)
np.savetxt('data_user/decrypted_data_cloud.csv', final_decypted.round(), delimiter=',')
# result_matrix = matrix - row_vector