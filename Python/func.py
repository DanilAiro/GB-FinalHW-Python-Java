from Note import Note as N
import sys
import os

notes = list()

def clean():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def add() -> None:
    note = N(input('Введите заголовок заметки: '),
             input('Введите тело заметки: '))
    notes.append(note)
    print('Заметка успешно создана!\n')


def show_list() -> None:
    for note in notes:
        print(f'{notes.index(note) + 1}. {note.__str__()}')
    print()


def show_note():
    return 0


def edit():
    return 0


def delete():
    return 0


def save():
    return 0


def start_program():
    isActive = True
    while isActive:
        print('Какую команду хотите выполнить?\n' +
              '1. Добавить заметку\n' +
              '2. Показать все заметки\n' +
              '3. Закрыть программу\n')
        command_str = input('Введите команду: ')
        if command_str.isdigit():
            command = int(command_str)

            match command:
                case 1:
                    add()
                case 2:
                    show_list()
                case 3:
                    isActive = False
                case _:
                    print('Команда не распознана\n')
        else:
            print(f'{command_str} не является числом\n')


def start_program_with_args(command: str, title: str, msg: str) -> None:
    print(2)


def main():
    clean()

    args = sys.argv

    if len(args) == 1:
        start_program()
    else:
        if len(sys.argv) < 6:
            print('Ошибка. Слишком мало параметров.')
            sys.exit(1)

        if len(sys.argv) > 6:
            print('Ошибка. Слишком много параметров.')
            sys.exit(1)

        start_program_with_args(args[3], args[5])
