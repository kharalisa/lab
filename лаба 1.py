slovar = {'0': 'ноль', '2': 'два', '4': 'четыре', '6': 'шесть'}

def number_to_words(number: str) -> str:
    return ' '.join(slovar[digit] if digit in slovar and int(digit) % 2 == 0 else digit for digit in number) #Функция, которая принимает строку number
#(представляющую число) и возвращает строку,
#где каждая цифра заменена на соответствующее слово из словаря DIGITS.

def process(filename: str):
    with open(filename, 'r') as file:
        data = file.read().split()

    numbers = [num for num in data if num.isdigit() and len(num) <= 5 and int(str(num)[0]) % 2 != 0 and all
               (c in '01234567' for c in num) ]

    for num in numbers:
        print(number_to_words(num))
process("numbers.txt")
