import sys

def main(args):
    if '--help' in args:
        print("Використання: python sys_tool.py [--help]")
        print("Виводить 'командна строка', якщо запущений через CLI.")
        print("Нічого не виводить при імпорті модуля.")
    else:
        print("командна строка")

if __name__ == "__main__":
    main(sys.argv[0:])