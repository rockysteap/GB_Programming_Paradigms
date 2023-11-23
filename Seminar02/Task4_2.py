# Процедурное программирование

# Список задач
tasks = []


# Функция для добавления задачи
def add_task():
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print("Задача добавлена.")


# Функция для просмотра задач
def view_tasks():
    print("Список задач:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")


# Функция для удаления задачи
def delete_task():
    view_tasks()
    index = int(input("Введите номер задачи для удаления: ")) - 1
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Задача '{deleted_task}' удалена.")
    else:
        print("Недопустимый номер задачи.")


# Функция для главного меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Недопустимый выбор. Пожалуйста, выберите действие из меню.")


# Вызов главного меню
main_menu()
