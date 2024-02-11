from logger import input_data, print_data, copy_record, delit_data

def interface():
    print('Добрый день, это Бот помощник.  \n'
          'Что Вы хотите сделать? \n'
          '1 – записать данные \n'
          '2 – вывести данные \n'
          '3 - записать данные в файл rez.txt \n'
          '4 - очистить данные')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 4:
        command = int(input('Повторите ввод, пожалуйста: '))


    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        copy_record()
    elif command == 4:
        delit_data()
        
interface()

