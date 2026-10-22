print("Калькулятор")

n1 = float(input("Введите первое число: "))
operation = input("Введите операцию +, -, *, /: ")
n2 = float(input("Введите второе число: "))

if operation == "+":
    result = n1 + n2
    print("Результат:", result, sep="")
elif operation == "-":
    result = n1 - n2
    print("Результат:", result, sep="")
elif operation == "*":
    result = n1 * n2
    print("Результат:", result, sep="")
elif operation == "/":
    if n2 == 0:
        print("Математическая ошибка!")
    else:
        result = n1 / n2
        print("Результат:", result, sep="")  
else:
    print("Ошибка! Неизвестная операция.")
