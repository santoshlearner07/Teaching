while True:
    sign1 = input("Select The sign rock,paper,scissor \n 0 to end game \n")
    sign2 = input("Select The sign rock,paper,scissor \n 0 to end game \n")

    if sign1 == "0" or sign2 == "0" :
        print("Game Ended")
        break

    
    if sign1 == sign2 :
        print("It was a Tie")
    elif sign1 == "rock":
        if sign2 == "scissor":
            print("Player 2 won the game")
        else:
            print("Player 1 won the game")
    elif sign1 == "scissor":
        if sign2 == "paper":
            print("Player 2 won the game")
        else:
            print("Player 1 won the game")
    elif sign1 == "paper":
        if sign2 == "rock":
             print("Player 2 won the game")
        else:
            print("Player 1 won the game")

    