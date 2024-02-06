# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

# Функция для замены символов в строке и сохранения изменений в файле
def replace_and_save(dir_name, filename):
    with open(dir_name + filename, 'r', encoding='utf-8', newline='\n') as file:
        lines = file.readlines()

    with open(dir_name + filename, 'w', encoding='utf-8', newline='\n') as file:
        for line in lines:
            if line.strip().startswith('{% include'):
                line = line.replace('\\', '/')
            file.write(line)


# Получаем список файлов с расширением .md в текущей директории
dir_name = 'D:\\WorkJob\\backups\\browser\\policy_test\\'
md_files = [file for file in os.listdir('D:\\WorkJob\\backups\\browser\\policy_test') if file.endswith('.md')]

# Проходим по каждому файлу, меняем символы и сохраняем изменения
for file in md_files:
    replace_and_save(dir_name=dir_name, filename=file)
