import random
print("Hi welcome to the guessing game. Please guess a number between 1 and 100")

guess = int(input("What is your guess?"))
correct_number =random.randint(1,100)
guess_count =0

while guess !=correct_number:
    guess_count+=1
    if guess<correct_number:
       guess = int(input("Wrong. You need to guess higher. What is your guess?"))
    else:
        guess = int(input("Wrong. You need to guess lower. What is your guess?"))


print(f"Congrats! The rigt answer was {correct_number}. It took you {guess_count} guess.")