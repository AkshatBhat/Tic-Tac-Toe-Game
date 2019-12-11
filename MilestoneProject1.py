def display_board(board):
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9]+' ')
    print('--- --- ---')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6]+' ')
    print('--- --- ---')
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3]+' ')
    

def player_input():
    print('Input will be asked again and again until correct data is fed!')
    player1_marker = ''
    player2_marker = ''
    player1_marker = input("Player 1 Choose 'X' or 'O': ")
    
    while player1_marker!='X' and player1_marker!='O':
        player1_marker = input("Player 1 Choose 'X' or 'O': ")
        
    if player1_marker=='X':
        player2_marker = 'O'
        print("Player 1 plays as 'X'")
        print("Player 2 plays as 'O'")
        return (player1_marker,player2_marker)
    else:
        player2_marker = 'X'
        print("Player 1 plays as 'O'")
        print("Player 2 plays as 'X'")
        return (player1_marker,player2_marker)
        
        

def place_marker(board, marker, position):
    if board[position]==' ':
        board[position] = marker
        
        
        
def win_check(board, mark):
    return mark==board[7]==board[8]==board[9] or mark==board[4]==board[5]==board[6] or mark==board[1]==board[2]==board[3] or mark==board[7]==board[4]==board[1] or mark==board[8]==board[5]==board[2] or mark==board[9]==board[6]==board[3] or mark==board[7]==board[5]==board[3] or mark==board[9]==board[5]==board[1]



from random import randint
def choose_first():
    return randint(1,2)
    
    
    
def space_check(board, position):
    if board[position]!=' ':
        return False
    else:
        return True
        
        
def full_board_check(board):
    for i in board[1:]:
        if i==' ':
            return False
    return True
    
    
def player_choice(i,z,board):
    move = int(input('Player {} --> {} your move position: '.format(i,z)))
    if space_check(board,move):
        return move
    else:
        return -1
        
flag = False
print('Welcome to Tic Tac Toe!')
test_board = ['@',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)
(p1,p2) = player_input()
first = choose_first()
print('At Random, Player {} will go first...'.format(first))

if first==1:
    
    while True:
        m1 = player_choice(1,p1,test_board)
        while (m1)==-1:
            print('Position already taken ...')
            m1 = player_choice(1,p1,test_board)
        place_marker(test_board,p1,m1)
        display_board(test_board)
        if win_check(test_board,p1):
            print("Player 1 has WON!!")
            flag = True
            break   
        if full_board_check(test_board):
            break
        
        m2 = player_choice(2,p2,test_board)
        while (m2)==-1:
            print('Position already taken ...')
            m2 = player_choice(2,p2,test_board)
        place_marker(test_board,p2,m2)
        display_board(test_board)
        if win_check(test_board,p2):
            print("Player 2 has WON!!")
            flag = True
            break
        if full_board_check(test_board):
            break
    if not flag:
        print("GAME DRAW!!")

if first==2:
        
    while True:
        m2 = player_choice(2,p2,test_board)
        while (m2)==-1:
            print('Position already taken ...')
            m2 = player_choice(2,p2,test_board)
        place_marker(test_board,p2,m2)
        display_board(test_board)
        if win_check(test_board,p2):
            print("Player 2 has WON!!")
            flag = True
            break
        if full_board_check(test_board):
            break
        
        m1 = player_choice(1,p1,test_board)
        while (m1)==-1:
            print('Position already taken ...')
            m1 = player_choice(1,p1,test_board)
        place_marker(test_board,p1,m1)
        display_board(test_board)
        if win_check(test_board,p1):
            print("Player 1 has WON!!")
            flag = True
            break 
        if full_board_check(test_board):
            break
    if not flag:
        print("GAME DRAW")        