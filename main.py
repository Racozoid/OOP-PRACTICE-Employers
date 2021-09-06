from classes import Staff

while True:
    print('\nЧто вы хотите?\nСписок комманд:')
    print('д -- добавить сотрудника\nу -- удалить сотрудника\nп -- показать данные последнего внесенного сотрудника')
    print('к -- показать колличество сотрудников\nи -- изменить долность сотрудника')
    command = input()
    if command == 'д':
        a = input('Введите ФИО: ')
        b = input('Введите зарплату: ')
        c = input('Введите должность: ')

        person = Staff(a, b, c)
        print('Пользователь {} добавлен'.format(a))
    elif command == 'к':
        Staff.displayCount()
    elif command == 'у':
        print('Work in progress. Данная функция будет добалена в следующих версиях.')
        person.__del__()
    elif command == 'п':
        if Staff.count < 1:
            print('Некого показывать')
            continue
        else:
            person.displayInfo()
    elif command == 'и':
        print('Work in progress. Данная функция будет добалена в следующих версиях.')
    else:
        print('Неверная команда')
    q = input('Хотите выйти? Если хотите, то напишите q\n--')
    if q == 'q':
        break




