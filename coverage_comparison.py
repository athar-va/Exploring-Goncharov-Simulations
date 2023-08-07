import numpy as np
import utility

def generate_random_points(d,n):
    # Initialize the points randomly on the unit sphere
    random_points = np.random.normal(size=(n, d))

    # Normalize the points for them to lie on a unit sphere
    random_points /= np.linalg.norm(random_points, axis=1)[:, np.newaxis]

    return random_points

def check_coverage(points):
    # Calculates the norm of the resultant Vector of all points
    result =np.zeros_like(points[1])

    for px in points:
        result += px

    return result

def avg_dist(points):
    # Calculates the average of the shortest distance between neighbours
    dist=Q3.pair_dist_print(points)
    print(dist)
    dist_set_wrt_point={}
    for i in range(len(points)):
        dist_set_wrt_point[i]=[]

    for i in range(len(points)):
        for j in dist.keys():
            if i in j:
                dist_set_wrt_point[i].append(round(dist[j],1))
    print(dist_set_wrt_point)

    min_dist=[]

    for i in dist_set_wrt_point:
        min_dist.append( min(dist_set_wrt_point[i]))

    print(min_dist)

    return sum(min_dist)/len(min_dist),np.var(min_dist)

n = 10
d = 3

random_points=generate_random_points(d,n)

goncharov_points = Q3.run_optimizer(d,n)

random_coverage=check_coverage(random_points)
goncharev_coverage=check_coverage(goncharov_points)

gon_avg_dist,gon_var_dist=avg_dist(goncharov_points)
random_avg_dist,random_var_dist=avg_dist(random_points)

print("Avg min dist in Random Points",random_avg_dist)
print("Avg min dist in Goncharov 3-config",gon_avg_dist,"\n")

print("Variance dist in Random Points",random_var_dist)
print("Variance dist in Gon",gon_var_dist,"\n")

print(" Norm of Resultant Vector of Random Points ", np.linalg.norm(random_coverage))
print("Norm of Resultant Vector of Goncharov 3-config ", np.linalg.norm(goncharev_coverage))