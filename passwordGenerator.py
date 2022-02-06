import random

print("PsyPass, faça sua password!")
nr_letters = int(input("Quantas letras conterá sua password?\n"))
nr_numbers = int(input("Quantos números?\n"))
nr_symbols = int(input("Quantos símbolos?\n"))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "$", "#", "%", "&", "*", "(", ")", "_", "+"]

password = ""

for letter in range(1, nr_letters + 1):
    # password += letters[random.randint(0,letter)]
    password += random.choice(letters)

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

pass_list =[]

pass_list[:0] = password
random.shuffle(pass_list)

passphrase = ""
for pass_char in pass_list:
    passphrase += pass_char

print(f"Aqui está sua senha!\n{passphrase}")