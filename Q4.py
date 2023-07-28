import math

import numpy as np

A = np.array([ 0.951511,   -0.28910735,  0.10508926])
B = np.array([-0.73079401, -0.68235473, -0.0182248 ])
C = np.array([-0.220717,    0.97146208, -0.08686446])

# Finds 3 vectors forming a triangle
AB_mag= np.linalg.norm(B-A)
BC_mag= np.linalg.norm(C-B)
AC_mag= np.linalg.norm(A-C)

# Calculates semiperimeter
s = (AB_mag+BC_mag+AC_mag)/2

print(s)

# Calculates area of the triangle usind semiperimeter
area= math.sqrt(s*(s-AB_mag)*(s-BC_mag)*(s-AC_mag))

print(area)