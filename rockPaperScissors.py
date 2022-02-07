import random

print("Rock, Paper or Scissors?")
your_choice = int(input("Pedra [0], papel [1] ou tesoura[2]?\n"))
computer_choice = random.randint(0, 3)

# print(computer_choice)

# if your_choice == "0":
#     print("pedra!")

# if your_choice == "1":
#     print("papel!")

# if your_choice == "2":
#     print("tesoura!")

# Test if is not 0, 1 or 2
if your_choice >= 0 and your_choice < 3:
    if your_choice == computer_choice:
        print(f"PC: {computer_choice}")
        print(f"Você: {your_choice}")
        print("Empate!")
    elif your_choice == 0 and computer_choice == 2:
        print(f"PC: {computer_choice}")
        print(f"Você: {your_choice}")
        print("Você ganhou!")
    elif your_choice == 2 and computer_choice == 0:
        print(f"PC: {computer_choice}")
        print(f"Você: {your_choice}")
        print("Você perdeu pro PC :/")
    elif your_choice > computer_choice:
        print(f"PC: {computer_choice}")
        print(f"Você: {your_choice}")
        print("Você ganhou!")
    elif computer_choice > your_choice:
        print(f"PC: {computer_choice}")
        print(f"Você: {your_choice}")
        print("Você perdeu pro PC :/")
else:
    print("Não leu não? É 0, 1 ou 2. Digita direito manolo!")