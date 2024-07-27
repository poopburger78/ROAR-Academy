
file_path = 'motto.txt'

with open(file_path, 'w') as file:
    file.write('Fiat Lux!\n')
with open(file_path, 'a+') as file:
    print(file.read()) #??
    file.write('Let there be light!')
    
