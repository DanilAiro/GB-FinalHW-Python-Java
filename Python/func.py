import Note as N

def add():
  return 0

def showList():
  return 0

def showNote():
  return 0

def edit():
  return 0

def delete():
  return 0

def save():
  return 0

def start_program():
  a = N.Note
  a.set_note(a, "Привет", "Данила")
  print(a.show_note(a))

def start_program_with_args(title: str, msg: str) -> None:
  print(2)