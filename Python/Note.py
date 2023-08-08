from datetime import datetime as date

class Note(object):
    def __init__(self, title, msg):
        self.__title = title
        self.__msg = msg
        self.__create_date = date.today()
        self.__update_date = date.today()

    def __str__(self) -> str:
        if self.__create_date != self.__update_date:
          return 'Заметка: {}, Тело заметки: {}, Дата создания: {}, Последняя дата изменения: {}'.format(self.__title, self.__msg, self.get_create_date(), self.get_update_date())
        else:
          return 'Заметка: {}, Тело заметки: {}, Время создания: {}'.format(self.__title, self.__msg, self.get_create_date())

    def set_title(self, title):
        self.__title = title
        self.set_update_date()

    def set_msg(self, msg):
        self.__msg = msg
        self.set_update_date()

    def set_create_date(self):
        self.__create_date = date.today()

    def set_update_date(self):
        self.__update_date = date.today()

    def get_title(self):
        return self.__title

    def get_msg(self):
        return self.__msg

    def get_create_date(self):
        return date.strftime(self.__create_date, '%d/%m/%Y, %H:%M:%S')

    def get_update_date(self):
        return date.strftime(self.__update_date, '%d/%m/%Y, %H:%M:%S')
