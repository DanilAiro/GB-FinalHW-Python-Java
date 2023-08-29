from Note import Note as N
import sys
import os
import json


def main() -> None:
    clean()
    print(notes)

    args = sys.argv

    if len(args) == 1:
        start_program()
    else:
        if len(sys.argv) < 3:
            print('Ошибка. Слишком мало параметров.')
            sys.exit(1)

        if len(sys.argv) == 4 or len(sys.argv) == 5:
            print('Ошибка. Неправильное количество параметров.')
            sys.exit(1)

        if len(sys.argv) > 6:
            print('Ошибка. Слишком много параметров.')
            sys.exit(1)

        if len(args) == 3 or len(args) == 6:
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
                    save()
                case _:
                    print('Команда не распознана\n')
        else:
            print(f'{command_str} не является числом\n')


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
            if args[2].isdigit():
                show_note(int(args[2]) - 1)
            else:
                for note in notes:
                    if note.get_title() == args[2]:
                        show_note(notes.index(note))
                        break
                else:
                    print('Нет такой заметки\n')
        case _:
            print('Команда указана неверно, повторите')
    save()


def clean() -> None:
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def fill_notes() -> list:
    file_str = 'notes.json'
    if os.path.exists(file_str):
        file = open(file_str, 'r')
        notes_str_list = file.read().split('\n')
        notes_list = list()
        for note in notes_str_list:
            if (not note.startswith('[') and not note.startswith(']')):
                print(1)
                note_list = note.split('; ')
                title = note_list[0]
                msg = note_list[1]
                creating_date = note_list[2]
                if len(note_list) == 4:
                    updating_date = note_list[3]
                    temp = N(title.removeprefix('"Title: '),
                             msg.removeprefix('Message: '))
                    temp.parse_note(creating_date.removeprefix('Creating date: ').replace('"', ''),
                                    updating_date.removeprefix('Updating date: ').replace('"', ''))
                else:
                    temp = N(title.removeprefix('"Title: '),
                             msg.removeprefix('Message: '))
                    temp.parse_note(creating_date.removeprefix('Creating date: ').replace('"', ''),
                                    creating_date.removeprefix('Creating date: ').replace('"', ''))
                notes_list.append(temp)
        return notes_list
    else:
        return list()


def add() -> None:
    note = N(input('Введите заголовок заметки: '),
             input('Введите тело заметки: '))
    notes.append(note)
    print('Заметка успешно создана!\n')


def auto_add(title: str, msg: str) -> None:
    note = N(title, msg)
    notes.append(note)
    print('Заметка успешно создана!\n')


def show_list() -> None:
    for note in notes:
        print(f'{notes.index(note) + 1}. {note.get_title()}')
    print()


def notes_menu() -> None:
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


def show_note(index_str: int) -> None:
    index = int(index_str) - 1
    if index < len(notes) and index >= 0:
        print(notes[index].__str__() + '\n')
        note_menu(index)
    else:
        print('Нет такой заметки\n')


def note_menu(index: int) -> None:
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


def edit(index: int) -> None:
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


def delete(index: int) -> None:
    if len(notes) > index and index >= 0:
        notes.pop(index)
        print('Заметка успешно удалена\n')
    else:
        print('Нет такой заметки')


def save() -> None:
    file_str = 'notes.json'
    json_notes = json.dumps([note.__str__()
                            for note in notes], indent=0, separators=['', ''])
    if json_notes != '[]':
        file = open(file_str, 'w')
        file.write(json_notes)
        file.close()
    else:
        if os.path.exists(file_str):
            os.remove(file_str)


notes = fill_notes()
