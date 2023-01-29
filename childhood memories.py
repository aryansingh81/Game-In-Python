import random

print("\t\t\t##WELCOME##")
print("\t🤟🏻🤟🏻🤟🏻🤟🏻#WHAT WOULD YOU LIKE TO PLAY#🤟🏻🤟🏻🤟🏻🤟🏻")
while True:
    a=int(input('''    (1) TIC-TAC-TOE
    (2) ✂️✂️ROCK-PAPER-SCISSOR✂️✂️
    (3) 🧍🧍HANGMAN🧍🧍
    (4) QUIT
    ENTER YOUR CHOICE : '''))
    if a == 1:
        # Function to print Tic Tac Toe
        def print_tic_tac_toe(values):
            print("\n")
            print("\t  {} | {} | {} ".format(values[0], values[1], values[2]))
            print("\t----+---+----")
            print("\t  {} | {} | {}".format(values[3], values[4], values[5]))
            print('\t----+---+----')
            print("\t  {} | {} | {} ".format(values[6], values[7], values[8]))
            print("\n")
        def tic_tac_toe_disc():
            print('here is the discription :\n enter the corresponding key to make the turn in that box...')
            print("\t  1 | 2 | 3")
            print("\t----+---+----")
            print("\t  4 | 5 | 6")
            print("\t----+---+----")
            print("\t  7 | 8 | 9")
        tic_tac_toe_disc()


        # Function to print the score-board
        def print_scoreboard(score_board):
            print("\t--------------------------------")
            print("\t              SCOREBOARD       ")
            print("\t--------------------------------")
 
            players = list(score_board.keys())
            print("\t   ", players[0], "\t    ", score_board[players[0]])
            print("\t   ", players[1], "\t    ", score_board[players[1]])
 
            print("\t--------------------------------\n")
 
        # Function to check if any player has won
        def check_win(player_pos, cur_player):
 
            # All possible winning combinations
            soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
            # Loop to check if any winning combination is satisfied
            for x in soln:
                if all(y in player_pos[cur_player] for y in x):
 
                # Return True if any winning combination satisfies
                    return True
            # Return False if no combination is satisfied       
            return False       
 
        # Function to check if the game is drawn
        def check_draw(player_pos):
            if len(player_pos['X']) + len(player_pos['O']) == 9:
                return True
            return False       
 
        # Function for a single game of Tic Tac Toe
        def single_game(cur_player):
 
            # Represents the Tic Tac Toe
            values = [' ' for x in range(9)]
     
            # Stores the positions occupied by X and O
            player_pos = {'X':[], 'O':[]}
        
            # Game Loop for a single game of Tic Tac Toe
            while True:
                print_tic_tac_toe(values)
         
                # Try exception block for MOVE input
                try:
                    print("Player ", cur_player, " turn. Which box? : ", end="")
                    move = int(input()) 
                except ValueError:
                    print("Wrong Input!!! Try Again")
                    continue
 
                # Sanity check for MOVE inout
                if move < 1 or move > 9:
                    print("Wrong Input!!! Try Again")
                    continue
 
                # Check if the box is not occupied already
                if values[move-1] != ' ':
                    print("Place already filled. Try again!!")
                    continue
 
                # Update game information
 
                # Updating grid status 
                values[move-1] = cur_player
 
                # Updating player positions
                player_pos[cur_player].append(move)
 
                # Function call for checking win
                if check_win(player_pos, cur_player):
                    print_tic_tac_toe(values)
                    print("\nPlayer ", cur_player, " has won the game!!🎉🎉🥳🥳")     
                    print("\n")
                    return cur_player
 
                # Function call for checking draw game
                if check_draw(player_pos):
                    print_tic_tac_toe(values)
                    print("Game Drawn")
                    print("\n")
                    return 'D'
 
                # Switch player moves
                if cur_player == 'X':
                    cur_player = 'O'
                else:
                    cur_player = 'X'
 
        if __name__ == "__main__":
 
            print("Player 1")
            player1 = input("Enter the name : ")
            print("\n")
 
            print("Player 2")
            player2 = input("Enter the name : ")
            print("\n")
     
            # Stores the player who chooses X and O
            cur_player = player1
 
            # Stores the choice of players
            player_choice = {'X' : "", 'O' : ""}
 
            # Stores the options
            options = ['X', 'O']
 
            # Stores the scoreboard
            score_board = {player1: 0, player2: 0}
            print_scoreboard(score_board)
 
            # Game Loop for a series of Tic Tac Toe
            # The loop runs until the players quit 
            while True:
 
                # Player choice Menu
                print("Turn to choose for", cur_player)
                print("Enter 1 for X")
                print("Enter 2 for O")
                print("Enter 3 to Quit")
 
                # Try exception for CHOICE input
                try:
                    choice = int(input("enter choice: "))   
                except ValueError:
                    print("Wrong Input!!! Try Again\n")
                    continue
 
                # Conditions for player choice  
                if choice == 1:
                    player_choice['X'] = cur_player
                    if cur_player == player1:
                        player_choice['O'] = player2
                    else:
                        player_choice['O'] = player1
 
                elif choice == 2:
                    player_choice['O'] = cur_player
                    if cur_player == player1:
                        player_choice['X'] = player2
                    else:
                        player_choice['X'] = player1
         
                elif choice == 3:
                    print("Final Scores")
                    print_scoreboard(score_board)
                    break  
 
                else:
                    print("Wrong Choice!!!! Try Again\n")
 
                # Stores the winner in a single game of Tic Tac Toe
                winner = single_game(options[choice-1])
         
                # Edits the scoreboard according to the winner
                if winner != 'D' :
                    player_won = player_choice[winner]
                    score_board[player_won] = score_board[player_won] + 1
 
                    print_scoreboard(score_board)
            # Switch player who chooses X or O
                if cur_player == player1:
                    cur_player = player2
                else:
                    cur_player = player1

    elif a == 2:
        # importing required random module
        print("The Rules of Rock paper scissor game will be follows: \n"
        +"Rock vs paper --> paper wins \n"
        +"Rock vs scissor --> Rock wins \n"
        +"paper vs scissor --> scissor wins \n")
        your_score=0
        comp_score = 0
        while True:
            print("Now please enter your choice no. \n 1. ROCK \n 2. PAPER \n 3. SCISSOR \n")
            # take the input from user
            ch = int(input("Now Your turn: "))
            while ch> 3 or ch< 1:
                ch = int(input("Enter your valid input here: "))
            if ch == 1:
                choice_name = 'ROCK'
            elif ch == 2:
                choice_name = 'PAPER'
            else:
                choice_name = 'SCISSOR'
            # print user given choice
            print("Your choice is: " + choice_name)
            print("\nNow its computer turn to initiate.......")
            # Computer will select randomly any number
            # among values 1, 2 and 3. Using randint method
            # of random module
            comp_choice = random.randint(1, 3)
            # loopingwill continue until comp_choice value
            # is equal to the choice value
            while comp_choice == ch:
                comp_choice = random.randint(1, 3)
            # initialize value of the variable comp_choice_name
            # variable corresponding to the choice value
            if comp_choice == 1:
                comp_choice_name = 'ROCK'
            elif comp_choice == 2:
                comp_choice_name = 'PAPER'
            else:
                comp_choice_name = 'SCISSOR'
            print("So computer choice is: " + comp_choice_name)
            print()
            print(choice_name + " V/s " + comp_choice_name)
            print()
            # condition for winning the game
            if((ch == 1 and comp_choice == 2) or (ch == 2 and comp_choice ==1 )):
                print("paper wins => ", end = "")
                final_result = "PAPER"
            elif((ch == 1 and comp_choice == 3) or (ch == 3 and comp_choice == 1)):
                print("Rock wins =>", end = "")
                final_result = "ROCK"
            else:
                print("scissor wins =>", end = "")
                final_result = "SCISSOR"
            # Printing either user or computer wins
            if final_result == choice_name:
                print("<== You are the winner ==>")
                print()
                your_score+=1
            else:
                print("<== Computer wins ==>")
                print()
                comp_score+=1
            print("\t\t##SCOREBOARD##")
            print("\tYOUR SCORE   COMP. SCORE")
            print("\t",your_score,"\t\t",comp_score)
            print("Do you want to play again? (Y/N)",end=':')
            ans = input()
            # if user input n or N then condition is True
            if ans == 'n' or ans == 'N':
                break
            # after exiting from the while loop
        print("\nThanks for sharing time with us...")
    
    elif a == 3:
        def hangman():
            name = input("What is your name? ")
            # Here the user is asked to enter the name first
 
            print("Good Luck ! ", name)
 
            words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
               
 
            # Function will choose one random
            # word from this list of words
            word = random.choice(words)
 
 
            print("Guess the characters")
 
            guesses = ''
 
            # any number of turns can be used here
            turns = 12
 
 
            while turns > 0:
     
                # counts the number of times a user fails
                failed = 0
     
                # all characters from the input
                # word taking one at a time.
                for char in word:
         
                    # comparing that character with
                    # the character in guesses
                    if char in guesses:
                        print(char,end=' ')
             
                    else:
                        print("_",end=' ')
             
                        # for every failure 1 will be
                        # incremented in failure
                        failed += 1
                
 
                if failed == 0:
                    # user will win the game if failure is 0
                    # and 'You Win' will be given as output
                    print("\nYou Win")
         
                    # this print the correct word
                    print("The word is: ", word)
                    break
     
                # if user has input the wrong alphabet then
                # it will ask user to enter another alphabet
                guess = input("\nguess a character:")
        
                    # every input character will be stored in guesses
                guesses += guess
     
                # check input with the character in word
                if guess not in word:
         
                    turns -= 1
         
                    # if the character doesn’t match the word
                    # then “Wrong” will be given as output
                    print("Wrong")
         
                    # this will print the number of
                    # turns left for the user
                    print("You have", + turns, 'more guesses')
         
         
                    if turns == 0:
                        print("You Loose")

        i='y'
        while i=='y' or i=='Y':
            hangman()
            i=input('want to play again?(y/n) : ')


    elif a == 4:
        print('\nTHANKS FOR PLAYING')
        break
    else :
        print("\nWROMG CHOICE!!!\nTRY AGAIN")
