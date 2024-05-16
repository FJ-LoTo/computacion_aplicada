import os

def menor(nums):
    m=nums[0]
    for n in range (len(nums)):
        if nums[n]<m:
            m=nums[n]
    return m

def leer():
    leidos=[]
    while True:
        d = int(input('numero? '))
        if d == -1: break
        leidos.append(d)
    return leidos

os.system('cls')
nums=leer()
menordetodos=menor(nums)
print('el menor es ', menordetodos)
