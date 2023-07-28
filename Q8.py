import numpy as np
import math
import Q3 as q
import pprint as pprint

result={}
d = 3



for n in range(1,21):

    # Generate n Goncharov d-configuration
    points=q.run_optimizer(d,n)
    print(points)

    # Generates distance between all the points
    dist=q.pair_dist_print(points)

    print(dist)

    # Generates dictionary with empty list as values
    dist_set_wrt_point={}
    for i in range(len(points)):
        dist_set_wrt_point[i]=[]

    # Generates sets of distances wrt all points
    for i in range(len(points)):
        for j in dist.keys():
            if i in j:
                dist_set_wrt_point[i].append(round(dist[j],4))
    print(dist_set_wrt_point)

    config_classes={}

    # Generates distinct sets
    for i in dist_set_wrt_point.keys():
        dist_set_wrt_point[i].sort()
        config_classes[tuple(dist_set_wrt_point[i])]=1

    pprint.pprint(config_classes)

    result[n]=sum(config_classes.values())
    n+=1


pprint.pprint(result)
