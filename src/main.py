def main():
    menu = (""" 
    1. Показать список задач.
    2. Добавить задачу.
    3. Удалить задачу.
    4. Выход.""")
    print(menu)
    user = input('Выбери пункт меню:')

    list_tasks = []

    if user == '1':
        print(list_tasks)

    if user == '2':
        task = input('Создать задачу: ')
        list_tasks += task

    if user == '3':
        list_tasks.pop(task)

    if user == '4':
        print(f'{menu}{user}')


def add_task():
    pass


def list_tasks():
    pass


def create_task():
    pass


def del_task():
    pass


if __name__ == '__main__':
    main()
