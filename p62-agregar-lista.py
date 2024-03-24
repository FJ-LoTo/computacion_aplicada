#cambiar o modificar los elementos de una lista

import os; os.system('cls')

print('aggregar elementos a una lista existente\n')
nums=[80.3,12.5,60.2,30.4]
print(f'todos {nums}, {len(nums)}')

print('agregar elementos al final')
nums.append(90)
nums.append(100)
print(f'todos {nums}, {len(nums)}')

print('insertar elementos en una posicion determinada')
nums.insert(4,80)
print(f'todos {nums}, {len(nums)}')

print('insertar elementos al final')
nums.extend([110,120,130])
print(f'todos {nums}, {len(nums)}')