import random
class TicTacToe:

#TIC-TAC-TOE GAME
    #Create board
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]

    '''
    As a Player would like to see the board so I can choose the valid cells during my turn
    '''
    def print_board(cls):
        for row in cls.board:
            print(row)

    #Play user
    def user_input(cls):
        print('user\'s turn...')
        try:
            __row = int(input('row : '))
            __column = int(input('Column : '))

            if __row > len(cls.board)-1 or __column > len(cls.board)-1:
                print('no!!,valuse should be less then this:{} '.format(len(cls.board)) )
                return cls.user_input()

        except ValueError as e:
            raise ValueError('plz enter correct row and colum')

        if cls.board[__row][__column] == " ":
            cls.board[__row][__column] = "X"
        else :
            print('user!! position already filled')
            cls.user_input()
   
    '''
    On Computer getting its turn would like the computer to play like me
    '''
    def computer_input(cls):
        print('computer\'s turn...')
        try:
            __row = random.randrange(0,3)
            __column = random.randrange(0,3)

            if __row > len(cls.board)-1 or __column > len(cls.board)-1:
                print('no!!,valuse should be less then this:{} '.format(len(cls.board)) )
                return cls.computer_input()
                
        except ValueError as e:
            raise ValueError('plz enter correct row and colum')

        if cls.board[__row][__column] == " ":
            cls.board[__row][__column] = "O"
        else :
            print('computer!! Position already filled')
            cls.computer_input()
    
    '''
    As player would expect the Tic Tac Toe App to determine after every move the winner or the tie or change the turn
    '''
    def check_win_user(cls):
        primary_doiagonal = 0
        secondary_diaggonal = 0
        for i in range(3):
            row = 0
            column = 0
            for j in range(3):
                if cls.board[i][j] == "X" : #Row win condition
                    row += 1
                if cls.board[j][i] == "X" : #column win condition
                    column += 1
                if i == j and cls.board[i][j] == "X" : #Primary diagonal win condition
                    primary_doiagonal += 1
                if i+j == 2 and cls.board[i][j] == "X" : #secondary diagonal win condition
                    secondary_diaggonal += 1
            if row == 3 or column == 3:
                return 1
                
        if secondary_diaggonal == 3 or primary_doiagonal == 3 :
            return 1
    '''
    As Computer would expect the Tic Tac Toe App to determine after every move the winner or the tie or change the turn
    '''
    def check_win_computer(cls):
        primary_doiagonal = 0
        secondary_diaggonal = 0
        for i in range(3):
            row = 0
            column = 0
            for j in range(3):
                if cls.board[i][j] == "O" : #Row win condition
                    row += 1
                if cls.board[j][i] == "O" : #column win condition
                    column += 1
                if i == j and cls.board[i][j] == "O" : #Primary diagonal win condition
                    primary_doiagonal += 1
                if i+j == 2 and cls.board[i][j] == "O" : #secondary diagonal win condition
                    secondary_diaggonal += 1
            if row == 3 or column == 3:
                return 1
        if secondary_diaggonal == 3 or primary_doiagonal == 3 :
            return 1
            
if __name__ == "__main__":
    
    tictack = TicTacToe()
    tictack.print_board()

    n = tictack.board.__len__()**2
    print('toss is happening...')
    
    '''
    As a Player would like to begin with a toss to check who plays first.
    '''
    if random.randint(0,1) == 0:
        print('you won the toss')
        tictack.user_input()
        tictack.print_board()
        tictack.computer_input()
        tictack.print_board()
        n -= 1
    else:
        print('computer won the toss')
        tictack.computer_input()
        tictack.print_board()

    n -= 1
    
    '''
    As a Player would play till the game is overUC 12 
    '''
    while n > 0 :
        
        
                tictack.user_input()
                n -= 1
                tictack.print_board()
                ret = tictack.check_win_user()
                if ret == 1 :
                    print('You won...')
                    break

            
                tictack.computer_input()
                n -= 1
                tictack.print_board()
                ret = tictack.check_win_computer()
                if ret == 1 :
                    print('computer won...')
                    break
