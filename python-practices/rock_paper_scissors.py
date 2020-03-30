user1 = input("What is your name?")
user2 = input("What about yours?")

user1_turn = input("%s, rock, paper or scissors " % user1).lower()
user2_turn = input("%s, rock, paper or scissors " % user2).lower()

def rock_paper_scissors(player1 , player2):
    if player1 == player2:
        print ("It`s a tie")
    elif player1 == "rock":
        if player2 == "scissors":
            print (user1, " wins")
        else:
            print (user2, " wins")
    elif player1 == "scissors":
        if player2 == "paper":
            print (user1 , " wins")
        else:
            print (user2, " wins")
    elif player1 == "paper":
        if player2 == "rock":
            print (user1, " wins")
        else:
            print (user2, " wins")
    else:
        print  ("Please Enter One of Which : Rock, Paper , Scissors")

rock_paper_scissors(user1_turn,user2_turn)
# Will work on replay
# Better version