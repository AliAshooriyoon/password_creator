import random

password = ""
lowwerCase = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "q",
    "y",
    "z",
]


opperCase = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "Q",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="]

num_of_lowwer_words = int(input("Wie viele Wörter soll Ihr Passwort enthalten?"))
num_of_opper_words = int(input("Wie viele große Wörter soll Ihr Passwort enthalten?"))
num_of_numbers = int(input("Wie viele Nummer soll Ihr Passwort enthalten?"))
num_of_symbols = int(input("Wie viele Symbols soll Ihr Passwort enthalten?"))

for word in range(num_of_lowwer_words):
    randLowWord = random.choice(lowwerCase)
    password += randLowWord
    # print(password)

for word in range(num_of_opper_words):
    randLowWord = random.choice(opperCase)
    password += randLowWord

for word in range(num_of_numbers):
    randLowWord = random.choice(numbers)
    password += randLowWord

for word in range(num_of_symbols):
    randLowWord = random.choice(symbols)
    password += randLowWord

print(password)
