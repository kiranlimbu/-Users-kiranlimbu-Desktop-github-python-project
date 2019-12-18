# note: made for notebook environment
from IPython.display import clear_output
import random
# Global Variables
players = [0,'X','O'] # players will input their symbol and that will be appended in the list. players1 == 1 and players2 == -1
player_num = [0, '1', '2']
num = [str(num) for num in range(0,10)]
my_lst = ['#'] # by using length of list, i can check if the board is full

def display_board(a):
    print('Numbers on the board are available positions\n\n\n' +
          ' '*15+'  ' +' |   |   \n' + 
          ' '*15+' ' +a[1]+' | '+a[2]+' | '+a[3]+' \n' + 
          ' '*15+'  ' +' |   |   \n' + 
          ' '*15+'-----------\n' + 
          ' '*15+'  ' +' |   |   \n' + 
          ' '*15+' ' +a[4]+' | '+a[5]+' | '+a[6]+' \n' + 
          ' '*15+'  ' +' |   |   \n' + 
          ' '*15+'-----------\n' + 
          ' '*15+'  ' +' |   |   \n' + 
          ' '*15+' ' +a[7]+' | '+a[8]+' | '+a[9]+' \n' + 
          ' '*15+'  ' +' |   |   \n')           
    
    
def place_marker(my_lst, num, position, marker):
    num[position] = marker
    my_lst.append(position)
            
            
def win_check(num,marker):

    return ((num[1] ==  num[2] ==  num[3] == marker) or # across the top
    (num[4] ==  num[5] ==  num[6] == marker) or # across the middle
    (num[7] ==  num[8] ==  num[9] == marker) or # across the bottom
    (num[1] ==  num[4] ==  num[7] == marker) or # down the middle
    (num[2] ==  num[5] ==  num[8] == marker) or # down the middle
    (num[3] ==  num[6] ==  num[9] == marker) or # down the right side
    (num[7] ==  num[5] ==  num[3] == marker) or # diagonal
    (num[9] ==  num[5] ==  num[1] == marker)) # diagonal


def random_player():
    return random.choice((-1, 1))
    

def full_board_check(my_lst):
    return len(my_lst) == 10


def player_choice(my_lst, player):
    position = 0
    
    while position in my_lst or position not in range(1,10):
        try:
            position = int(input('Player %s, Enter your next move: (1-9) '%(player)))
        except:
            print('Invalid input, please try again.')
    
    return position

def player_input(players):  #returns what player 1 selected. Teacher version does not allow player to select
    player_id = '0'
    
    while player_id not in players:
        try:
            player_id = input('Player %s, select X or O: '%(player)).upper()
        except:
            print('Invalid selection!')
            
    for i in range(1,3):
        if players[i] == player_id:
            if i == 2:
                return -1
            else:
                return 1

            
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    clear_output()
    print('Welcome to Tic Tac Toe Game!')

    #toggle = random_player()
    player = player_num[1]
    player_id = player_input(players)
    sign = player_id

    toggle = random_player()

    if toggle == 1:
        sign = player_id
    else:
        sign *= -1
    
    player = player_num[toggle]
    marker = players[sign]

    clear_output()
    print('Player %s goes first\n'%player)

    game_on = True
    input('Hit Enter to continue')
    while game_on:
    
        display_board(num)
        position = player_choice(my_lst, player)
        place_marker(my_lst, num, position, marker)
    
        if win_check(num,marker):
            clear_output()
            display_board(num)
            print('Congratulation! Player %s won the game.'%(player))
            game_on = False
        else:
            if full_board_check(my_lst):
                clear_output()
                display_board(num)
                print("It's a Draw!")
                break
            else:
                toggle *= -1
                sign *= -1
                player = player_num[toggle]
                marker = players[sign]
                clear_output()

    # reset board
    num = [str(num) for num in range(0,10)]
    my_lst = ['#']
    
    if not replay():
        break