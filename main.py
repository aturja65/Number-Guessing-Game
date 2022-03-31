from random import randint
difficulty={
    "Easy":10,
    "Medium":5,
    "Hard":3
}


def answer_checker(num,answer):
    if num>answer:
        print("Too high")
        return False
    elif num==answer:
        print(f"You've guessed the right number\nThe right answer is {num}")
        return True
    else:
        print("Too low")
        return False


level = input("Welcome to the guessing game\nPlease choose a difficulty level: 'Easy', 'Medium', 'Hard'\n")
guess=difficulty[level]
print(f"You've {guess} guesses so you better make them count")
num=int(input("Please guess a number between 1 to 100: "))
answer=randint(1,100)
while guess>0:
    if not answer_checker(num,answer):
        guess-=1
        print(f"You've {guess} guess left")
        num=int(input("Please guess another number: "))
    else:
        break
if guess==0:
    print("You loose")