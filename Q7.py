# for 3 dimensions
import numpy as np
import math
import Q3 as q
import pprint

# Find all the angles in a triangle represented by ABC
def find_angle(A,B,C):
    points=[]
    angles =[]
    a = B-A
    b = C-A

    a_unit=a/np.linalg.norm(a)
    b_unit=b/np.linalg.norm(b)
    angle=math.degrees(np.arccos(np.dot(a_unit,b_unit)))

    points.append([B,A,C])
    angles.append(angle)

    a = A - B
    b = C - B

    a_unit = a / np.linalg.norm(a)
    b_unit = b / np.linalg.norm(b)
    angle = math.degrees(np.arccos(np.dot(a_unit, b_unit)))

    points.append([A,B,C])
    angles.append(angle)

    a = B - C
    b = A - C

    a_unit = a / np.linalg.norm(a)
    b_unit = b / np.linalg.norm(b)
    angle = math.degrees(np.arccos(np.dot(a_unit, b_unit)))



    points.append([B,C,A])
    angles.append(angle)

    return points,angles

d = 3
n = 5

# Generate n Gonocharaov d config
points = q.run_optimizer(d,n)
print(points)

# Generate distance between all points
dist=q.pair_dist_print(points)
print("Distances")
pprint.pprint(dist)

point_id_map = {}
for i in range(len(points)):
    point_id_map[i] = points[i]

pprint.pprint(point_id_map)

point_set={}

# Generate all combinations of points where A,B,C = C,B,A = C,A,B
for i in point_id_map.keys():
    for j in point_id_map.keys():
        if i!=j:
            for k in point_id_map.keys():
                if i!=k and j!=k:
                    li=[i,j,k]
                    # print(li)
                    li.sort()
                    # print(li)
                    point_set[tuple(li)]=1

pprint.pprint(point_set)

# Generate angles in triangles
all_points=[]
angles=[]
for i in point_set.keys():
    px,ax=find_angle(point_id_map[i[0]],point_id_map[i[1]],point_id_map[i[2]])
    for j in range(len(px)):
        all_points.append(px[j])
        angles.append(ax[j])

print(angles)
# print(all_points)
# for i in range(len(angles)):
#     print(angles[i],"Points :",all_points[i],"\n")






