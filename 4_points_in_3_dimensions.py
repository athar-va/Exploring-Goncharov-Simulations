import numpy as np

A=np.array([0.28760963,  0.94255252, -0.16992774])
B=np.array([ 0.4376796,  -0.33691351,  0.83362213])
C=np.array([ 0.26823903, -0.57486551, -0.77303135])
D=np.array([-0.99352827, -0.03077351,  0.10933697])

# Group 3 points and formulate 2 vectors
AB= A-B
BC= B-C
DC= D-C

# performs A.(BxC)
print(np.dot(np.cross(AB,BC),DC))




