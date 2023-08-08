class Note:
    def __init__(self):
        self.__title
        self.__msg

    def set_note(self, title, msg):
        self.__title = title
        self.__msg = msg

    def set_title(self, title):
        self.__title = title

    def set_msg(self, msg):
        self.__msg = msg

    def get_title(self):
        return self.__title
    
    def get_msg(self):
        return self.__msg
        
