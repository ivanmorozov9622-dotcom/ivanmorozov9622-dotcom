import random

print("Игра угадай-ка")

number = random.randint(1,100)
attemps = 0

while True:
    guess = int(input("Попробуйте угадать число от 1 до 100:"))
    attemps += 1

    if guess < number:
        print("Загаданное число больше")
    elif  guess > number:
         print("Загаданное число меньше")
    else:
         print("Вы угадали число", number) 
         print("Вам понадобилось" , attemps, "попыток")    
         break
             
