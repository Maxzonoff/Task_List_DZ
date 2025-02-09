def main():
    menu = (""" 
    1. Показать список задач.
    2. Добавить задачу.
    3. Удалить задачу.
    4. Выход.""")
    print(menu)
    user = input('Выбери пункт меню:')
    while user != '4':
        print(menu)
        user = input('Выбери пункт меню: ')
    if user == '1':
        list_tasks()

    if user == '2':
        return create_task()

    if user == '3':
        pass


def add_task():
    list_tasks = []
    list_tasks += create_task()


def list_tasks(list_tasks):
    print(list_tasks)


def create_task():
    task = input('Создать задачу: ')
    return task


def del_task():
    pass


if __name__ == '__main__':
    main()
