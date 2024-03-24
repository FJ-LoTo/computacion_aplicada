#cambiar o modificar los elementos de una lista

import os; os.system('cls')

nums=[10,9,8,5,6.5,9.8,7.5,6.2,9.50]
print('modificar los elementos de una lista \n')
print(f'todos {nums}, {len(nums)}')
print('modificar los elementos 0 y 1')
nums[0] = 7; nums[1] = 7
print(f'todos {nums}, {len(nums)}')
print('modificar los elementos del 2 al 5')
nums[2:5] = [9,9,9]
print(f'todos {nums}, {len(nums)}')