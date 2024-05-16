import os
import datetime, calendar

os.system('cls')
print('sistema operativo', os.uname())
print('carpeta actual', os.getcwd())
os.chdir('/')
print(os.listdir())
print('\nla fecha actual:', ahora.strftime('%b / %d / %Y'))
print('\nla fecha actual: ', ahora.strftime('%H:%M'))
      
print('\nCalendario anual 2024:\n')
calendar.prcal(2024)
print('\nCalendario de un mes especifico')
calendar.prmonth(2024,4)