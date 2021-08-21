enter_symbols = []#список для вводимых координат символов для исключения повторного ввода
stroke_number = 0 #переменная для поочередного вывода крестика и нолика
symbol = None #переменная, определяющая, что будет: крестик или нолик
print('Добро пожаловать в игру "Крестики - нолики". Да начнется битва')
def beetwen_(): #функция для печати разделительной полосы
    print('_________________________________________________________________________________________________________')
pole = ['   a b c\n', 'a', '1', '2', '3','\n','b', '4',  '5',  '6','\n', 'c', '7',  '8',  '9']
beetwen_()
print(*pole)
beetwen_()

def enter():# функция для ввода координот игрового символа
    global stroke_number#объявление глобальных переменных
    global symbol
    global pole
    a = input('Введите номер места для вашего символа (от 1 до 9):\n')
    #ввод игроком координат своего символа
    if a.isalpha():
        print('Неверный формат')
        enter()
    elif 0 < int(a) < 10 and a not in enter_symbols:#проверка на корректность вводимых данных(от 1 до 9) и на неповторяемость
        stroke_number += 1# увеличиваем на 1, чтобы поменять символ через четность - нечетность
        enter_symbols.append(a)
        if stroke_number % 2 == 1:  # определяем какой символ будет выведен:крестик или нолик (четный крестик, нечетный нолик)
            symbol = '0'
        else:
            symbol = 'x'
        for i in pole:
            if i == a:
                pole[pole.index(i)] = symbol
    elif a in enter_symbols:
        print('Данное место уже занято')
        enter()#возврат к началу функции для повторного ввода координат, если введены данные, по которым символ в игровом поле уже стоит
    else:
        print('Вы ввели неверные данные (за пределами игрового поля)')
        enter()#возврат к началу функции, если введены неверные координаты
    print(*pole)

enter()
print(symbol)
enter()
print(symbol)
enter()
print(symbol)
enter()
print(symbol)
enter()
print(symbol)
enter()
print(symbol)
enter()
print(symbol)
enter()
print(symbol)
enter()
print(symbol)
print(enter_symbols)



