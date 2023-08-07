import numpy as np
import math
import utility as q
import pprint as pprint

result={}
d = 4


# Prints distances between points for each of the set configurations
for n in range(1,7):

    points=q.run_optimizer(d,n)
    # print(points)
    dist=q.pair_dist_print(points)

    print("Distances for",n,"points in",d,"dimensions")
    pprint.pprint(dist)
