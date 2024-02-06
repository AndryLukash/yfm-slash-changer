
import PySimpleGUI as sg
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


sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Будем менять "\\" на "/"')],
      [sg.Text('Выбор каталога:', size=(15, 1)), sg.InputText(key='-text-'), sg.FolderBrowse()],
      [sg.Button('OK', enable_events=True, key='-FUNCTION-', font='Helvetica 10'), sg.Cancel()] ]






window = sg.Window('md slash changer', layout)

# запускаем основной бесконечный цикл
while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
    # если нажали на кнопку
    if event == '-FUNCTION-':
        # запускаем связанную функцию
        dir_name = values['-text-']
        # print(dir_name)
        #dir_name = dir_name.replace('/', '\\')
        dir_name = dir_name + "/"
        # print(dir_name)
        md_files = [file for file in os.listdir(dir_name) if file.endswith('.md')]
        print(md_files)
        # Проходим по каждому файлу, меняем символы и сохраняем изменения
        for file in md_files:
            replace_and_save(dir_name=dir_name, filename=file)
        sg.popup('Готово!')
    
# закрываем окно и освобождаем используемые ресурсы
window.close()