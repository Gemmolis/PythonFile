from data_create import input_user_data 

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'В каком формате записать данные?\n'
                    f'1 вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    'Ваш выбор: '
                    ))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'  
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 вариант:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file: 
        data = file.readlines() 
        print(''.join(data))  
        
    print('2 вариант:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

def copy_record():
    f1 = open("data_second_variant.csv", "r")
    f2 = open("rez.txt", "w")
    line = f1.readline()
    while line:
        new_lines = line.replace(";", "\n")
        f2.write(new_lines)
        line = f1.readline()    
    f1.close()
    f2.close()
    print('Файл rez.txt записан')

def delit_data():
    m = int(input('Какой файл очистить? '))
    if m == 1:
        with open('data_first_variant.csv', 'w+', encoding='utf-8') as file:
            file.write('')
    else:
        with open('data_second_variant.csv', 'w+', encoding='utf-8') as file:
            file.write('')
