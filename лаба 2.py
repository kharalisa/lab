import re
slovar = {'0': 'ноль', '2': 'два', '4': 'четыре', '6': 'шесть'}

def number_to_words(number: str) -> str:
    return ' '.join(slovar[digit] if digit in slovar and int(digit) % 2 == 0 else digit for digit in number) #Функция, которая принимает строку number
#(представляющую число) и возвращает строку,
#где каждая цифра заменена на соответствующее слово из словаря DIGITS.

def process(filename: str):
    with open(filename, 'r') as file:
        a = file.read()

    numbers = re.findall(r'\b[0-7]{1,5}\b', a)# Регулярное выражение для поиска всех восьмеричных чисел
        # (состоящих только из цифр 0-7) идлиной от 1 до 5

    numbers = [num for num in numbers if int(str(num)[0]) % 2 != 0]

    for num in numbers:
        print(number_to_words(num))
process("numbers.txt")
