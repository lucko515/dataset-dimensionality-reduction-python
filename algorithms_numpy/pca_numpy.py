import numpy as np

def PCA_numpy(data, n_components=2):
    
    #1nd step is to find covarience matrix
    data_vector = []
    for i in range(data.shape[1]):
        data_vector.append(data[:, i])
    
    cov_matrix = np.cov(data_vector)
    
    #2rd step is to compute eigen vectors and eigne values
    eig_values, eig_vectors = np.linalg.eig(cov_matrix)
    eig_values = np.reshape(eig_values, (len(cov_matrix), 1))
    
    #Make pairs
    eig_pairs = []
    for i in range(len(eig_values)):
         eig_pairs.append([np.abs(eig_values[i]), eig_vectors[:,i]])
    
    eig_pairs.sort()
    eig_pairs.reverse()
    
    #This PCA is only for 2 components
    reduced_data = np.hstack((eig_pairs[0][1].reshape(len(eig_pairs[0][1]),1), eig_pairs[1][1].reshape(len(eig_pairs[0][1]),1)))
                      
    return data.dot(reduced_data)