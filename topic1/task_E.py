# E. Точка и треугольник

def euclid_dist_my(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2


def tri_area(d,x,y):
    if x >= 0 and y >= 0 and y <= d-x:
        return 0
    dist = [euclid_dist_my(x,y,0,0), euclid_dist_my(x,y,d,0), euclid_dist_my(x,y,0,d)]
    return dist.index(min(dist))+1

d = int(input())
x,y = tuple(map(int, input().split()))
print(tri_area(d,x,y))
