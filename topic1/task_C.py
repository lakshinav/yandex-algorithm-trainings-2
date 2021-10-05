# C. Даты

def is_correct_date(x,y,z):
    if (x > 12 or y > 12) or (x == y):
        return 1
    return 0

print(is_correct_date(*tuple(map(int, input().split()))))
