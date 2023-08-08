import sys
import func

args = sys.argv

if len(args) == 1:
    func.start_program()
else:
    if len(sys.argv) < 6:
        print("Ошибка. Слишком мало параметров.")
        sys.exit(1)

    if len(sys.argv) > 6:
        print("Ошибка. Слишком много параметров.")
        sys.exit(1)

    func.start_program_with_args(args[3], args[5])
