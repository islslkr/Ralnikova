number = input("Введите число:")
polyndrom = tuple(number)
if ( polyndrom == polyndrom [::-1]): 
    print('О да, это палидром!') 
else: 
    print('Неет, это точно не палидром')











# напоминалка для склерозника(меня): [::-1]  (напр: 899 [0(начало числа):4(последнее число по счету):-1(начнет идти с конца выражения)])