print("Добро пожаловать в калькулятор")
firstNumber = int(input("Введите первое чисо:" + ""))
print("Выбирите нужную операцию: "+" ")
operation=input("При нажатии 0 будет выведена сумма чисел \n  1- разность чисел \n 2 -произведение чисел \n 3-частное чисел \n 4-возведение в степень ")
if operation==0:
   secondsummand =int(input("Введите второе сллагаемое:"+" "))
   print("Сумма введенных вами чисел равна:"+" "+str(firstNumber+secondsummand))
elif operation=="1":
    deductible= int(input("введите вычитаемое:"+""))
    print("Разность введенных вами чисел равна:"+" "+str(firstNumber-deductible))
elif operation=="2":
   multiplier = int(input("введите второе число" + " "))
   print("произведение ваших чисел равно:"+" "+str(firstNumber+secondNumber))
#elif operation=="3":
    #secondNumber = int(input("введите второе число" + " "))
    #print("Частное ваших чисел сотавляет:"+" "+str(firstNumber//secondNumber))
#elif operation=="4":
    #extent=int(input("Введите степень,в которую хотите возвести число"))
   # print("Ваше число во введенной степени равно:"+" "+str(firstNumber))