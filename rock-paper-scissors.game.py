import random
global users_score
user_score = 0


def select(random_pass, user):
    users_score  = 0
    
    if random_pass == user:
        print("It's Tie")

    elif random_pass == "Rock":
        if user == "Scissors":
            print("You Loose")
        if user == "Paper":
            users_score += 1
            print("You Win")


    elif random_pass == "Paper":
        if user == "Scissors":
            print("You Loose")
        if user == "Rock":
            users_score += 1
            print("You Win")


    elif random_pass == "Scissors":
        if user == "paper":
            print("You Loose")
        if user == "Rock":
            users_score += 1
            print("You Win")

    elif random_pass not in choice:
        print("Wrong input")
    return users_score 

while True:

    
    choice = ["Rock", "Paper", "Scissors"]

    random_pass = random.choice(choice)
    user = input("Whats your choice to given in these passes \n 1: Rock \n 2: Paper \n 3: Scissors \n")
    print("Your choice is : ", user,"\n")
    print("Computer choice is : ", random_pass,"\n")
    
    select(random_pass, user)

    
    user_input = input(" 1: Score\n 2: Try Again\t\t")
    if user_input == "1":
        user_score += int(select(random_pass, user))
        print(f"Your Score is {user_score}\n")

    



