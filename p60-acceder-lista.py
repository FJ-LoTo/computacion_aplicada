#acceder a los elementos de una lista

import os; os.system('cls')
nums = [10,20,30,40,60,70,10,20,99]

print('acceder a los elementos de una lista\n')
print(f'la lista tiene {len(nums)} elementos')
print(f'la lista completa: {nums}')
print(f'Primero: {nums(0)}, ultimo: {nums(8)}')
print(f'Primero: {nums(-9)}, ultimo: {nums(-1)}')
print(f'los primeros tres: {nums[:3]}')
print(f'los ultimos tres: {nums[6:]}')