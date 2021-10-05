# B. Кольцевая линия метро

def min_stations_cnt(n,i,j):
    return min(
        abs(i-j)-1,
        n-max(i,j) + min(i,j) - 1
    )

print(min_stations_cnt(*tuple(map(int, input().split()))))
