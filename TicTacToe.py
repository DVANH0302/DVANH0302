import random 

class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2 
        self.starter = None
        self.role1 = ""
        self.role2 = ""
        self.board = [str(i) for i in range(1,10)]       
        self.winner = None
    
    def decide_starter(self):
        choice = random.randint(1, 2)
        if choice == 1:
            self.starter = self.player1
        else:
            self.starter = self.player2

    def X_or_O(self):
        choice = random.randint(1, 2)
        if choice == 1:
            self.role1 = "X"
            self.role2 = "O"
        else:
            self.role1 = "O"
            self.role2 = "X"
        
    def print_board(self):
        for i in range(0,9,3):
            print(self.board[i] + " | " + self.board[i+1] + " | " + self.board[i+2])
            print("_________")
            print()
    
    def check_winner(self):
        # Column and Row
        for i in range(0,3):
            if self.board[i] == self.board[i+3] == self.board[i+6]:
                self.winner = self.board[i]
                return True      
            elif self.board[i*3] == self.board[i*3 +1] == self.board[i*3 +2]:
                self.winner = self.board[i]
                return True
        # Diagonal
        if self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]:
            self.winner = self.board[4]
            return True            
            
    def PlayTheGame(self):
        game = TicTacToe(self.player1, self.player2)
        game.decide_starter()
        game.X_or_O()
        print(game.player1 + " is " + game.role1)
        print(game.player2 + " is " + game.role2)
        print("Let's begin!")
        game.print_board()
        for i in range(9):
            print(game.starter + "'s turn:", end =" ")
            choice = int(input())
            if game.starter == game.player1:
                game.board[choice-1] = game.role1
                game.starter = game.player2
            else:
                game.board[choice-1] = game.role2
                game.starter = game.player1
            game.print_board()
            if i>=4:
                check = game.check_winner()
                if check == True:
                    if game.winner == game.role1:
                        game.winner = game.player1
                    else:
                        game.winner = game.player2
                    print("The winner is " + game.winner + ' !!!!')
                    break
        if game.winner == None:
            print("This is a Tie")

TicTacToe("Vanh", "Funny Guy").PlayTheGame()

          