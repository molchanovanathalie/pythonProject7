# Урок 7. Файлы и файловая система
# Создайте функцию, которая создаёт файлы с указанным расширением. Функция
# принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
#
# Чтобы записать байты можно использовать список с числами и функцию bytes


import random
import string
from random import choice, randint



def start_file(files = 4, len_name_min = 6, len_name_max = 30, len_text_min = 256, len_text_max = 4096 ):
    extension = 'txt'
    for _ in range(files):
        file_name = ''
        for _ in range(randint(len_name_min, len_name_max)):
            file_name = file_name + choice(string.ascii_lowercase)
        with open(f'{file_name}.{extension}', 'w') as f:
            for _ in range(randint(len_text_min, len_text_max)):
                f.write(f'{bytes(randint(1, 9))} \n')
    return



# параметры в ручную:
# files = int(input('введите количество генерируемых файлов: '))
# len_name_min = int(input('введите  минимальную длину случайно сгенерированного имени: '))
# len_name_max = int(input('введите  максимальную длину случайно сгенерированного имени: '))
# len_text_min = int(input('введите  минимальное число случайных байт, записанных в файл: '))
# len_text_max = int(input('введите  максимальное число случайных байт, записанных в файл: '))

start_file()









