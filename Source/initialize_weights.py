import numpy as np
import os
import time
import json

start = time.time()

cwdPath = os.getcwd()
cwdPath = cwdPath.replace("Source", "NN_Info")

with open(cwdPath + '/nn_info') as f: 
    info = f.read() 

info_dict = json.loads(info) 

#number of layers
L = int(info_dict["L"])

#number of sets of weights matrices
WEIGHTS_SETS = L - 1

cwdPath = os.getcwd()
cwdPath = cwdPath.replace("Source", "Weights")

#list of weights matrices dimensions
#make sure you have enough dimensions set in the file
WEIGHTS_DIMS = list(np.loadtxt(cwdPath + "/weights_dims", dtype='int', delimiter=','))


for i in range(WEIGHTS_SETS):
    w = np.random.rand(WEIGHTS_DIMS[i][0],WEIGHTS_DIMS[i][1])
    file_name = '../Weights/w' + str(i)
    np.savetxt(file_name, w, delimiter=',')

end = time.time()
print("Elapsed time [s]: " + str(end- start))