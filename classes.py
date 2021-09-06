class Staff:
    """Класс работников"""
    count = 0

    def __init__(self, name, pay, position):
        """Тут должны как бы храниться данные, но у меня не хватает знаний для этого"""
        self.name = name
        self.pay = pay
        self.position = position
        Staff.count += 1

    # Нужно куда-то складировать данные, пока как это сделать я не заню :)

    def displayInfo(self):
        """Вывод последнего введенного сотрудника"""
        print('Фио:', self.name)
        print('Зарплата:', self.pay)
        print('Должность:', self.position)

    def displayCount(self):
        """Вывод колличества сотрудников"""
        print('Колличество сотрудников:', Staff.count)

    def __del__(self):
        """Пока что просто минусует единичку. Пока что бессполезен по сути"""
        Staff.count -= 1

