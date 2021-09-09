print("Добро пожаловать в калькулятор")
firstNumber = int(input("Введите первое чисо:" + ""))
operation=input(" Выбирите нужную операцию. При нажатии 0 будет выведена сумма чисел \n  1- разность чисел \n 2 -произведение чисел \n 3-частное чисел \n 4-целочисленное деление\n 5- остаток от делкения\n 6-возведеение в степень \n")
if operation=="0":
   secondsummand =int(input("Введите второе сллагаемое:"+" "))
   print("Сумма введенных вами чисел равна:"+" "+str(firstNumber+secondsummand))
elif operation=="1":
    deductible= int(input("введите вычитаемое:"+""))
    print("Разность введенных вами чисел равна:"+" "+str(firstNumber-deductible))
elif operation=="2":
   multiplier = int(input("Ввведите второй множитель: " + " "))
   print("Произведение ваших чисел равно:"+" "+str(firstNumber*multiplier))
elif operation=="3":
    f_divisior = int(input("Введите делитель:" + " "))
    f_division_result=firstNumber/f_divisior  #  переменная содержит число с плавающей точкой
    print("Частное ваших чисел сотавляет:"+" "+str(f_division_result))
elif operation=="4":
    i_divisior=int(input("Введите делитель:"+""))
    i_division_result=firstNumber//i_division  # переменная содержит целое число
    print("Частное ваших чисел сотавляет:"+" "+str(i_division_result))
elif operation=="5":
    r_divisior=int(input("Введите делитель:"+" "))
    r_division_result=firstNumber%r_divisior
    print("Остаток от деления ваших чисел равен:"+""+str(r_division_result))
elif operation=="6":
    extent=int(input("Введите степень,в которую хотите возвести число"))
    print("Ваше число во введенной степени равно:"+" "+str(firstNumber**extent))
