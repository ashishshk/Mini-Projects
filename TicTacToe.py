board = ['','','','','','','','',''] 

def display_board(board):
    print(board[0] + '  | ' + board[1] + ' | ' + board[2] )
    print('--' + ' ' + '---' + ' ' + '---')
    print(board[3] + '  | ' + board[4] + ' | ' + board[5] )
    print('--' + ' ' + '---' + ' ' + '---')
    print(board[6] + '  | ' + board[7] + ' | ' + board[8] )
    
def player_choice():
    temp = 0
    while (temp == 0):
        inp1 = input('Player 1 please enter your choice(Either X or O): ')
        if inp1 == 'X' or inp1 == 'O':
            temp += 1
        else:
            print("\nYou haven't entered either X or O!")
            temp += 0
    if inp1 == 'X':
        inp2 = 'O'
    else:
        inp2 = 'X'
    print("Player1 has selected: " + inp1)
    print("Player2 has selected: " + inp2)
    return inp1
    
ch1 = player_choice()

if ch1 == 'X':
    ch2 = 'O'
else:
    ch2 = 'X'
    
def disp_numpad():
    print('0' + ' | ' + '1' + ' | ' + '2' )
    print('--' + ' ' + '---' + ' ' + '---')
    print('3' + ' | ' + '4' + ' | ' + '5' )
    print('--' + ' ' + '---' + ' ' + '---')
    print('6' + ' | ' + '7' + ' | ' + '8' )
    
print('The game is about to begin...\n')
print('Player 1 will go first...\n')
print('Please enter the location on which you want to place your piece, by referring to the numpad displayed below: \n')
disp_numpad()

def place_marker1():
    print("\nIt's Player1's turn...\n")
    pos1 = int(input('\n\nEnter your choice of location now: \n'))
    if board[pos1] == '' :
        board[pos1] = ch1
    else:
        temp = []
        print('That location is already occupied! Please re-enter...')
        for i in range(0,len(board)):
            if board[i] == '':
                temp.append(i)
        print("your available locations are... ")
        print(temp)
        pos2 = int(input('\n\nEnter your choice of location now: \n'))
        board[pos2] = ch1
    display_board(board)
    print('\n')
    
def place_marker2():
    print("\nIt's Player2's turn...\n")
    pos2 = int(input('\nEnter your choice of location now: \n'))
    if board[pos2] == "":
        board[pos2] = ch2
    else:
        temp = []
        print('That location is already occupied! Please re-enter...')
        for i in range(0,len(board)):
            if board[i] == '':
                temp.append(i)
        print("your available locations are... ")
        print(temp)
        pos2 = int(input('\n\nEnter your choice of location now: \n'))
        board[pos2] = ch1
    display_board(board)
    print('\n')
    
def has_won():
    if board[6] == board[7] == board[8] == ch1:
            print('\nPlayer1 has won!')
            return True
    elif board[6] == board[7] == board[8] == ch2:
        print('\nPlayer2 has won!:')
        return True
    elif board[0] == board[1] == board[2] == ch1:
            print('\nPlayer1 has won!')
            return True
    elif board[0] == board[1] == board[2] == ch2:
        print('\nPlayer2 has won!:')
        return True
    elif board[3] == board[4] == board[5] == ch1:
            print('\nPlayer1 has won!')
            return True
    elif board[3] == board[4] == board[5] == ch2:
        print('\nPlayer2 has won!')
        return True
    elif board[0] == board[3] == board[6] == ch1:
            print('\nPlayer1 has won!')
            return True
    elif board[0] == board[3] == board[6] == ch2:
        print('\nPlayer2 has won!')
        return True
    elif board[1] == board[4] == board[7] == ch1:
            print('\nPlayer1 has won!')
            return True
    elif board[1] == board[4] == board[7] == ch2:
        print('\nPlayer2 has won!')
        return True
    elif board[2] == board[5] == board[8] == ch1:
            print('\nPlayer1 has won!')
            return True
    elif board[2] == board[5] == board[8] == ch2:
        print('\nPlayer2 has won!:')
        return True
    elif board[0] == board[4] == board[8] == ch1:
            print('\nPlayer1 has won!')
            return True
    elif board[0] == board[4] == board[8] == ch2:
        print('\nPlayer2 has won!:')
        return True
    elif board[2] == board[4] == board[6] == ch1:
            print('\nPlayer1 has won!')
            return True
    elif board[2] == board[4] == board[8] == ch2:
        print('\nPlayer2 has won!:')
        return True
    else:
        return False
    
    
while True:
    place_marker1()
    if has_won() == True:
        break
    place_marker2()
    if has_won() == True:
        break
    
