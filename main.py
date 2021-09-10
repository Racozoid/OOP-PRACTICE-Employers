workers = dict()    # Словарь в котором хранятся работники


def someSort():
    # Сортировка списка по ФИО
    global workers
    list_workers = list(workers.items())
    list_workers.sort(key= lambda i: i[1][0])
    sworkers = dict()
    j = 1
    for i in list_workers:
        sworkers[j] = workers[i[0]]
        j += 1
    workers = sworkers


while True:
    print('\n\nСписок команд:\nq -- выход\nadd -- добавить сотрудника\nshow -- показать список сотрудников'
          '\ndel -- удалить сотрудника')
    command = input('Введите команду: ')
    if command == 'q':
        break
        # Выход из программы

    elif command == 'add':
        # Добавит нового сотрудника в словарь с сотрудниками
        name = input('\nВведите ФИО: ')
        pos = input('Введите должность: ')
        try:    # Проверка на неверные значения зарплаты
            cash = int(input('Введите зарплату: '))
        except ValueError:
            print('Введено некорректное значение! Попробуйте снова')
            continue
        else:
            if cash < 0:
                # Проверка на отрицательные числа
                print('Некорректная заработная плата. Попробуйте снова.')
                continue
            workers[len(workers) + 1] = (name, pos, cash)
        someSort()  # Сортировка после добавления сотрудника

    elif command == 'show':
        # Вывод таблицы с работниками и их количества
        if len(workers) != 0:   # Проверка на то есть ли работники
            print('\n№ : личные данные')
            for i in workers:
                print(i, ':', workers[i][0], '\n\tДолжность:', workers[i][1], '\n\tЗарплата:', workers[i][2])
        print('\nКоличество сотрудников:', len(workers))

    elif command == 'del':
        # Удаление работника из словаря
        d = int(input('\nВведите № сотрудника для удаления: '))
        del workers[d]
        someSort()  # Сортировка после удаления
