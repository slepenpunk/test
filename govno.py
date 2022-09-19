def ask_y_n(question):
    ask = None
    while ask not in ('y', 'n'):
        ask = input(question).lower()
    return ask


def new_file(name):
    open(name, 'a', encoding='utf=8')


def change_file(name):
    try:
        file = open(name, 'r+', encoding='utf=8')
        change = input('Enter new data: ')
        file.write(change)
        file.write('\n')
    except FileNotFoundError:
        print('This file is not found!')


def read_file(name):
    try:
        read_the_file = open(name, 'r', encoding='utf=8')
        print(read_the_file.read())
    except FileNotFoundError:
        print('This file is not found!')


def main():
    choice = None
    while choice != '0':
        print('''
MESHOK  0 - Exit
  TI    1 - Create new file
PIDOR   2 - Read file
!!!!!!  3 - Change file 
        ''')
        choice = input('Enter you variation: ')
        if choice == '0':
            break

        elif choice == '1':
            enter = input('Enter name for new file(.txt): ')
            new_file(enter)
            print('-' * 20)
        elif choice == '2':
            file = input('Enter name file: ')
            read_file(file)
            print('-' * 20)
        elif choice == '3':
            ask = None
            while ask != 'n':

                ask = ask_y_n('Do you want enter new data?(y/n): ')
                if ask == 'n':
                    break
                elif ask == 'y':
                    file = input('Enter the file to change it: ')
                    change_file(file)
                    print('-' * 20)

main()