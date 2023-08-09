from Note import Note as N
import sys
import os

notes = list()


def main() -> None:
    clean()

    args = sys.argv

    if len(args) == 1:
        start_program()
    else:
        # if len(sys.argv) < 6:
        #     print('Ошибка. Слишком мало параметров.')
        #     sys.exit(1)

        if len(sys.argv) > 6:
            print('Ошибка. Слишком много параметров.')
            sys.exit(1)

        if len(args) == 3 or len(args) == 4 or len(args) == 6:
            start_program_with_args(args)


def start_program() -> None:
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
                    if len(notes) != 0:
                        notes_menu()
                    else:
                        print('Нет заметок\n')
                case 3:
                    isActive = False
                case _:
                    print('Команда не распознана\n')
        else:
            print(f'{command_str} не является числом\n')


# добавить методы для разных задачь: удалить, обновить, показать. По названию и по номеру
def start_program_with_args(args) -> None:
    match args[1]:
        case 'add':
            if args[2] == '--title' and args[4] == '--msg':
                auto_add(args[3], args[5])
            elif args[2] == '--msg' and args[4] == '--title':
                auto_add(args[5], args[3])
            else:
                print('Аргументы указаны неверно, повторите')
        case 'delete':
            if args[2].isdigit():
                index = int(args[2])
                delete(index - 1)
            else:
                for note in notes:
                    if note.get_title() == args[2]:
                        delete(notes.index(note))
                        break
                else:
                    print('Нет такой заметки\n')
        case 'show':
            pass
        case 'update':  # добавить редактирование названия или тела
            if args[2] == '--old' and args[4] == '--new':
                auto_add(args[3], args[5])
            elif args[2] == '--new' and args[4] == '--old':
                auto_add(args[5], args[3])
            else:
                print('Аргументы указаны неверно, повторите')
        case _:
            print('Команда указана неверно, повторите')


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


def auto_add(title, msg) -> None:
    note = N(title, msg)
    notes.append(note)
    print('Заметка успешно создана!\n')


def show_list() -> None:
    for note in notes:
        print(f'{notes.index(note) + 1}. {note.get_title()}')
    print()


def notes_menu():
    print('1. Показать заметку\n' +
          '2. Назад\n')
    command_str = input('Введите команду: ')
    if command_str.isdigit():
        command = int(command_str)

        match command:
            case 1:
                show_note(input('Введите номер заметки: '))
            case 2:
                pass
            case _:
                print('Команда не распознана\n')
    else:
        print(f'{command_str} не является числом\n')


def show_note(index_str) -> None:
    if index_str.isdigit():
        index = int(index_str)
        if index <= len(notes):
            print(notes[index - 1].__str__() + '\n')
            note_menu(index - 1)
        else:
            print('Нет такой заметки\n')
    else:
        print(f'{index_str} не является числом\n')


def note_menu(index):
    print('1. Редактировать заметку\n' +
          '2. Удалить заметку\n' +
          '3. Назад\n')
    command_str = input('Введите команду: ')
    if command_str.isdigit():
        command = int(command_str)

        match command:
            case 1:
                edit(index)
            case 2:
                delete(index)
            case 3:
                show_list()
                if len(notes) != 0:
                    notes_menu()
                else:
                    print('Нет заметок\n')
            case _:
                print('Команда не распознана\n')
    else:
        print(f'{command_str} не является числом\n')


def edit(index) -> None:
    print('1. Редактировать название\n' +
          '2. Редактировать тело\n' +
          '3. Назад\n')
    command_str = input('Введите команду: ')
    if command_str.isdigit():
        command = int(command_str)

        match command:
            case 1:
                notes[index].set_title(input('Введите новое название: '))
                print('Название обновлено успешно\n')
            case 2:
                notes[index].set_msg(input('Введите новое тело: '))
                print('Тело обновлено успешно\n')
            case 3:
                show_note(index)
            case _:
                print('Команда не распознана\n')
    else:
        print(f'{command_str} не является числом\n')


def delete(index) -> None:
    notes.pop(index)
    print('Заметка успешно удалена\n')


def save() -> None:
    return 0
