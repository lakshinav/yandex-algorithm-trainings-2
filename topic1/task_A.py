# A.Interactor

def Interactor(returncode, interactor, checker):
    if interactor == 0 and returncode != 0:
        return 3
    if interactor == 0 and returncode == 0:
        return checker
    if interactor == 1:
        return checker
    if interactor == 4 and returncode != 0:
        return 3
    if interactor == 4 and returncode == 0:
        return 4
    if interactor == 6:
        return 0
    if interactor == 7:
        return 1
    return interactor

returncode = int(input())
interactor = int(input())
checker = int(input())
print(Interactor(returncode, interactor, checker))
