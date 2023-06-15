import os
import hashlib


dir_folder = input("Введите путь до папки:         Пример: 'C:/user'")
list_files, hash_list, checklist = [],[],[]


for address, dirs, files in os.walk(dir_folder):
    for name in files:
        list_files.append(os.path.join(address, name))  # Создание списка файлов


def hash_file(filename):
    """"This function returns the SHA-1 hash
     of the file passed to variable filename"""


    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    hash_list.append(h.hexdigest())


for i in range(len(list_files)):  # Запуск функции с перебором по файлам
    hash_file(list_files[i])

checklist = [(list_files[i], hash_list[i]) for i in range(len(list_files))]

file = open('checklist.txt', 'w')
for j in checklist:
    line = ''.join(str(x+' ') for x in j)
    file.write(line + '\n')
file.close()
