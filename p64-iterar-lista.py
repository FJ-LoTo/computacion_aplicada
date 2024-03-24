#iterar sobre los elementos de una lista

import os; os.system('cls')

nums=[2,4,6,8,10,12,14,16]

print('iterar por los elementos de una lista')
print(f'los numeros {nums}, {len(nums)}')

print('iterar usando for: ')
for num in nums:
    print('#:', num)

print('iterar por indice')
for i in range(len(nums)):
    print('>', nums[i], nums[i]*3)

print('iterar por indice y elevar al cuadrado')
for i in range(len(nums)):
    nums[i] = nums[1]**2
    print('>', nums[i])