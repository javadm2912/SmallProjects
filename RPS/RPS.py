import random

choices = ["rock","paper","scissors"]

while True:
    user = input("Please choose rock or paper or scissors : ")

    while user not in choices:
        print(user + " Not Valid Retry ....")
        user = input("Please choose rock or paper or scissors : ")

    computer = random.choice(choices)

    print("you : " + user)
    print("Computer : " + computer)

    if computer == user:
        print("TIE PLAY AGAIN")
    elif (user == "paper" and computer == "scissors") or (user == "rock" and computer == "paper") or (user == "scissors" and computer == "rock"):
        print("YOU LOSE !!!!!")
    elif (user == "paper" and computer == "rock") or (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper"):
        print("YOU WIN !!!!!")

#TANKS FOR WATHING
#PLEASE LIKE AND SUBSCRIBE   