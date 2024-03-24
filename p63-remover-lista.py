#remover elementos de una lista

import os; os.system('cls')

nums=[80.3,12.5,60.2,30.4]

print('remover elementos de una lista\n')
print(f'todos {nums}, {len(nums)}')

print('remover la primera pcurrencia de un elemento de una lista\n')
nums.remove(99)
print(f'todos {nums}, {len(nums)}')

print('remover un elemento con pop en una posicion determinada y regresarlo\n')
num = nums.pop(8)
print(f'todos {nums}, {len(nums)}, eliminado: {num}')
      
print('remover el ultimo elemento usando pop\n')
num = nums.pop()
print(f'todos {nums}, {len(nums)}, eliminado: {num}')

print('borrar todos los elementos de una lista\n')
nums.clear()
print(f'todos {nums}, {len(nums)}')
