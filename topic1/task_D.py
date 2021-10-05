# D. Строительство школы

# some cheat))
from statistics import median_high

def school(homes):
    return median_high(homes)


n = int(input())
homes = list(map(int, input().split()))
print(school(homes))
