#!/usr/bin/python3
import subprocess

# a. Копировать файл `dz1.py` в файл `dz1_run.py`
subprocess.run('cp dz1_1.py dz1_run.py', shell=True)

# b. Делать так чтобы он мог запуститьсся из bash
subprocess.run('chmod u+x dz1_run.py', shell=True)
result_1 = subprocess.run(['ls', '-ld', 'dz1_run.py'], capture_output=True, text=True)
print(f'access -> {result_1.stdout}')

# c. Менять права доступа к нему на:
# Доступ полностью запрещен для всех кроме овнера
# Овнер может читать и запускать файл
subprocess.run(['chmod u+rx,g=,o= dz1_run.py'], shell=True)
result1_2 = subprocess.run(['ls', '-ld', 'dz1_run.py'], capture_output=True, text=True)
print(f'access -> {result_1.stdout}')

# d. Запускать файл `dz1_run.py`
subprocess.call('./dz1_run.py', shell=True)
