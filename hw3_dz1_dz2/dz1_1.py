#!/usr/bin/python3
import random
import subprocess

# a. Выводить имя текущего пользователя
subprocess.run('whoami')

# b. Выводить путь к текущей директории
subprocess.run('pwd')

# c. Создавать папку `dz1` в текущей директории
subprocess.run('mkdir dz1', shell=True)

# d. В папке `dz1` создавать файлы для каждого дня текущего месяца в формате `dd-mm-yyyy.log`(список файлов для
# создания должен создаваться с помощью генератора в python)
create_file = ['touch']
file_name = ['./dz1/' + f'{i:0{2}}' + '-11-2022.log' for i in range(1, 30+1)]
create_file.extend(file_name)
subprocess.run(create_file)

# e. менять овнера папки `dz1` и всех файлов в ней на пользователя `root`
subprocess.run('sudo chown -R root ./dz1', shell=True)
result = subprocess.run(['ls', '-ld', './dz1'], capture_output=True, text=True)
print(result.stdout)

# f. удалять 5 случайных файлов из папки `dz1`
result = subprocess.run(['ls', 'dz1'], capture_output=True, text=True)
files = result.stdout.split('\n')
files.remove('')
delete_files_command = ['rm']
while True:
    file_names_2 = set('./dz1/' + random.choice(files) for i in range(5))
    if len(file_names_2) != 5:
        continue
    else:
        delete_files_command.extend(file_names_2)
        print(delete_files_command)
        subprocess.run(delete_files_command)
        break

