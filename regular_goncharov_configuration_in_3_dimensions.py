# for 3 dimensions
import numpy as np
import math
import utility as q
from itertools import combinations

# Generates angles
def find_angle(A,B,C):
    a = B-A
    b = C-A

    a_unit=a/np.linalg.norm(a)
    b_unit=b/np.linalg.norm(b)
    return math.degrees(np.arccos(np.dot(a_unit,b_unit)))


d = 3
n = 4

# Generates n Goncharov d-configuration
points=q.run_optimizer(d,n)
print(points)
dist=q.pair_dist_print(points)

angle=[]
co_ords=[]

# For 3 points
# angle1=find_angle(points[0],points[1],points[2])
# angle2=find_angle(points[2],points[0],points[1])
# angle3=find_angle(points[1],points[2],points[0])
# print(angle1,angle2,angle3)

# For 4 points
angle1=find_angle(points[3],points[0],points[1])
angle2=find_angle(points[3],points[1],points[2])
angle3=find_angle(points[3],points[2],points[0])

angle4=find_angle(points[0],points[1],points[3])
angle5=find_angle(points[0],points[1],points[2])
angle6=find_angle(points[0],points[2],points[3])

angle7=find_angle(points[1],points[0],points[2])
angle8=find_angle(points[1],points[0],points[3])
angle9=find_angle(points[1],points[3],points[0])

angle10=find_angle(points[2],points[0],points[1])
angle11=find_angle(points[2],points[0],points[3])
angle12=find_angle(points[2],points[3],points[1])

print(angle1,angle2,angle3,angle4,angle5,angle6,angle7,angle8,angle9,angle10,angle11,angle12)