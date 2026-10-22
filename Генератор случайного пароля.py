import random
import string

#Алфавит случайного пароля
characters = string.ascii_letters + string.digits + "!@#$%^&*"

print("Генератор пароля")
length = int(input("Введите количество символов желаемой длины пароля:"))

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Ваш пароль:", password)
