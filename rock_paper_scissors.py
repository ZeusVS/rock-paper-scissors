import random

possible_moves = ["R", "P", "S"]
move_names = ["Rock", "Paper", "Scissors"]

score = [0, 0, 0]

def win():
    print("Player Wins!")
    score[0] += 1
    show_score()

def lose():
    print("Player Loses!")
    score[1] += 1
    show_score()

def tie():
    print("It's a tie!")
    score[2] += 1
    show_score()

def show_score():
    print("Wins: " + str(score[0]))
    print("Losses: " + str(score[1]))
    print("Ties: " + str(score[2]))

# Keep playing until player wants to (Q)uit
while True:
    # Get player's input
    while True:
        player_move = input("(R)ock, (P)aper or (S)cissors?\n(Q) to quit\n").upper()
        if player_move == "Q":
            quit()
        if player_move in possible_moves:
            print("Player move: " + move_names[possible_moves.index(player_move)])
            break
        else:
            print("Unexpected input")

    # Get computer's input
    computer_move = possible_moves[random.randint(0,2)]
    print("Computer move: " + move_names[possible_moves.index(computer_move)])

    if player_move == computer_move:
        tie()

    if player_move == "R":
        if computer_move == "S":
            lose()
        else:
            win()
    elif player_move == "P":
        if computer_move == "R":
            lose()
        else:
            win()
    else:
        if computer_move == "P":
            lose()
        else:
            win()