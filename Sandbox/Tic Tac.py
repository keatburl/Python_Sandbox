board = [" " for i in range(9)]

def print_board():
 row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
 row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
 row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])
 print()
 print(row1)
 print(row2)
 print(row3)
 print() 

def player_moves(icon):
    if icon == "X":
      number = 1
     
    elif icon == "O": 
      number = 2
    print("Your turn player {}.".format(number))

    choice = int(input("Select your move (1-9):").strip())
    if board[choice-1]==" ":
     board[choice-1]=icon
    else:
        print("This space is already taken")
        print("Choose another space")

def victory(icon):
    if (board[0]== icon and board[1]== icon and board[2]==icon) or\
       (board[3]== icon and board[4]== icon and board[5]==icon) or\
       (board[6]== icon and board[7]== icon and board[8]==icon) or\
       (board[0]== icon and board[4]== icon and board[8]==icon) or\
       (board[0]== icon and board[3]== icon and board[6]==icon) or\
       (board[1]== icon and board[4]== icon and board[6]==icon) or\
       (board[2]== icon and board[5]== icon and board[8]==icon) or\
       (board[2]== icon and board[4]== icon and board[6]==icon):
           return True
    else:
               return False
def draw():
    if " " not in board:
        return True
    else:
        return False
    
while True:
 print_board()
 player_moves("X")
 if victory("X"):
  print_board()   
  print("Player 1 is Victorious!")
  break
 elif draw():
  print("It's a draw")
  break
 print_board()
 player_moves("O")
 if victory("O"):
  print_board()   
  print("Player 2 is Victorious!")
  break
 elif draw():
  print("It's a draw")
  break
 

