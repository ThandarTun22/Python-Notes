
class Board():

    def __init__(self):
        self.cells = [ "", " ", " ", " "," ", " "," ", " "," ", " ",]
        # self.cells = [ "", " X", " O", " X"," X", " O","O ", " O"," X", " O",]

    # displaying the tic-tac-toe board by using some print functions
    def display(self):

        print("{} | {} | {}".format(self.cells[1], self.cells[2], self.cells[3]))
        
        print("----------")
        print("{} | {} | {}".format(self.cells[4], self.cells[5], self.cells[6]))
        print("----------")
        
        print("{} | {} | {}".format(self.cells[7], self.cells[8], self.cells[9]))

    # update the cells list with 'X' or 'O' if user chooses a cell number
    def update_cells(self, cel_num, player):
        self.cells[cel_num] = player
        self.display()

    # checking the empty cell
    # return true uf there is an empty cell
    def space_check(self, cell_num):
        if self.cells[cell_num] == ' ':
            return True

    
    # checking the winner
    def is_winner(self, player):
        if   ( self.cells[1] == player and self.cells[2] == player and self.cells[3] == player ): 
            return True
        elif ( self.cells[4] == player and self.cells[5] == player and self.cells[6] == player ):
            return True
        elif ( self.cells[7] == player and self.cells[8] == player and self.cells[9] == player ):
            return True 
        elif ( self.cells[1] == player and self.cells[4] == player and self.cells[7] == player ):
            return True
        elif ( self.cells[2] == player and self.cells[5] == player and self.cells[8] == player ):
            return True
        elif ( self.cells[3] == player and self.cells[6] == player and self.cells[9] == player ):
            return True
        elif ( self.cells[1] == player and self.cells[5] == player and self.cells[9] == player ):
            return True 
        elif ( self.cells[3] == player and self.cells[5] == player and self.cells[7] == player ):
            return True 
        else:
             return False

    # checking tie or not
    def is_tie(self):
        #  if ( self.cells[1] != ' ' and self.cells[2] != ' ' and self.cells[3] != ' ' and self.cells[4] != ' ' and
        #  self.cells[5] != ' ' and self.cells[6] != ' ' and  self.cells[7] != ' ' and self.cells[18] != ' ' and self.cells[9] != ' ' ):
        #     return True 

         return not (" " in self.cells)

    # reseting the bord
    def reset(self):
        self.cells = [ "", " ", " ", " "," ", " "," ", " "," ", " ",]

board = Board()

def print_header():
    print("Welcome to Tic-Tac-Toe Game! \n")

def refresh_screen():

    # clearing the output screen
    print("\n" * 100)

    # decorating the game
    print_header()

    # display our board
    board.display()


while True:

    # refresh the screen
    refresh_screen()

    # x turn
    choice = 0
    
    while choice not in [1,2,3,4,5,6,7,8,9] or not board.space_check(choice) :
        
        choice = int(input('X :Please Enter 1 to 9 :'))

    # update cells
    board.update_cells(choice, "x")

    # test winner
    if board.is_winner("x"):
        # refresh_screen()
        print("x win")
        play_again = input('Do you want to play again (y/n)? : ').upper()
        # if play again
        if play_again == 'Y':
            # reset the board
            board.reset()
            continue
        else:
            break

    # refresh the screen
    refresh_screen()

    if board.is_tie():
        print("Draw! ")
        play_again = input('Do you want to play again (y/n)? : ').upper()
        # if play again
        if play_again == 'Y':
            # reset the board
            board.reset()
            continue
        else:
            break
    # o turn
    choice = 0  
    while choice not in [1,2,3,4,5,6,7,8,9] or not board.space_check(choice):
        
        choice = int(input('O : Please Enter 1 to 9 :'))

    # update cells
    board.update_cells(choice, "O")

    # test winner
    if board.is_winner("O"):
        # refresh_screen()
        print("O win")
        play_again = input('Do you want to play again (y/n)? : ').upper()
        # if play again
        if play_again == 'Y':
            # reset the board
            board.reset()
            continue
        else:
            break
