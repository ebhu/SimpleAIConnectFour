#create board
board = [' ' for _ in range(42)]


def display_board(board):
  """function to display the board"""
  for i in range(6):
    print('|', board[i*7], '|', board[i*7 + 1], '|', board[i*7 + 2], '|', board[i*7 + 3], '|', board[i*7 + 4], '|', board[i*7 + 5], '|', board[i*7 + 6], '|')
  print('-' * 29)

def evaluate_board(board, ai_player):
  """function that evaluates if either player has won
  """
  if check_win(board, ai_player):
    return 10
  elif check_win(board, 'R' if ai_player == 'Y' else 'Y'):
    return -10
  else:
    # Encourage winning moves and discourage losing moves (heuristic)
    empty_cells = [i for i, x in enumerate(board) if x == ' ']
    return 0# Ongoing game

def player_move(board, player):
  """This function handles the human player's move. It keeps prompting the player for a valid move (1-42) until a valid selection is made."""
  while True:
    move = int(input(f"Player {player}, enter your move (1-42): ")) - 1
    if 0 <= move <= 41 and (move>=35 or board[move+7]!=' ') and board[move] == ' ':
      board[move] = player
      break
    else:
      print("Invalid move. Try again.")

def generate_win_conditions():
    win_conditions = []

    # Horizontal win conditions
    for row in range(6):
        for col in range(4):  # Only need to check starting from the first 4 columns
            start = row * 7 + col
            win_conditions.append((start, start + 1, start + 2, start + 3))

    # Vertical win conditions
    for col in range(7):
        for row in range(3):  # Only need to check starting from the first 3 rows
            start = row * 7 + col
            win_conditions.append((start, start + 7, start + 14, start + 21))

    # Diagonal (positive slope) win conditions
    for row in range(3):
        for col in range(4):
            start = row * 7 + col
            win_conditions.append((start, start + 8, start + 16, start + 24))

    # Diagonal (negative slope) win conditions
    for row in range(3):
        for col in range(4):
            start = (row + 3) * 7 + col
            win_conditions.append((start, start - 6, start - 12, start - 18))

    return win_conditions

win_conditions = generate_win_conditions()

def check_win(board, player):
  """This function checks if a player has won the game by looking for matching markers in any of the eight winning conditions (rows, columns, diagonals)."""
  """ win_conditions = (
        # Horizontal win conditions
        (0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6),
        (7, 8, 9, 10), (8, 9, 10, 11), (9, 10, 11, 12), (10, 11, 12, 13),
        (14, 15, 16, 17), (15, 16, 17, 18), (16, 17, 18, 19), (17, 18, 19, 20),
        (21, 22, 23, 24), (22, 23, 24, 25), (23, 24, 25, 26), (24, 25, 26, 27),
        (28, 29, 30, 31), (29, 30, 31, 32), (30, 31, 32, 33), (31, 32, 33, 34),
        (35, 36, 37, 38), (36, 37, 38, 39), (37, 38, 39, 40), (38, 39, 40, 41),

        # Vertical win conditions
        (0, 7, 14, 21), (7, 14, 21, 28), (14, 21, 28, 35),
        (1, 8, 15, 22), (8, 15, 22, 29), (15, 22, 29, 36),
        (2, 9, 16, 23), (9, 16, 23, 30), (16, 23, 30, 37),
        (3, 10, 17, 24), (10, 17, 24, 31), (17, 24, 31, 38),
        (4, 11, 18, 25), (11, 18, 25, 32), (18, 25, 32, 39),
        (5, 12, 19, 26), (12, 19, 26, 33), (19, 26, 33, 40),
        (6, 13, 20, 27), (13, 20, 27, 34), (20, 27, 34, 41),

        # Diagonal (positive slope) win conditions
        (14, 22, 30, 38), (7, 15, 23, 31), (0, 8, 16, 24), (8, 16, 24, 32), (1, 9, 17, 25), (9, 17, 25, 33), (2, 10, 18, 26), (10, 18, 26, 34), (3, 11, 19, 27),
        (21, 15, 9, 3), (28, 22, 16, 10), (22, 16, 10, 4), (35, 29, 23, 17), (29, 23, 17, 11), (23, 17, 11, 5), (36, 30, 24, 18), (30, 24, 18, 12), (24, 18, 12, 6),

        # Diagonal (negative slope) win conditions
        (3, 9, 15, 21), (4, 10, 16, 22), (10, 16, 22, 28), (5, 11, 17, 23), (11, 17, 23, 29), (17, 23, 29, 35), (6, 12, 18, 24), (12, 18, 24, 30), (18, 24, 30, 36),
        (0, 8, 16, 24), (1, 9, 17, 25), (2, 10, 18, 26), (3, 11, 19, 27), (7, 15, 23, 31), (8, 16, 24, 32), (9, 17, 25, 33), (10, 18, 26, 34),
  )"""
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False


def main():
  """The main method for making moves and outputting wins or ties"""
  current_player = 'R'  # Human starts first
  game_over = False
  depth = 5  # Adjust this for AI difficulty (higher depth = more intelligent but slower)
  ai_player = 'Y'  # Set AI player to 'Y'

  while not game_over:
    display_board(board)

    # Human player's turn
    if current_player == 'R':
      player_move(board, current_player)

    # AI player's turn
    else:
      move = get_ai_move(board, ai_player, depth)
      board[move] = current_player
      print(f"AI Player ({ai_player}) moved to position {move + 1}")  # Positions start from 1 for user

    # Check for winner or tie
    if check_win(board, current_player):
      display_board(board)
      print(f"Player {current_player} wins!")
      game_over = True
    else:
      if all(x != ' ' for x in board):
        print("It's a tie!")
        game_over = True
      current_player = 'Y' if current_player == 'R' else 'R'


def minimax(board, depth, ai_player, maximizing_player):
  """This method uses recursion to simulate the outcomes of different
    moves and then backtracks to find the best next move"""

  # Base case: Terminal state or max depth reached
  if depth == 0 or check_win(board, ai_player) or check_win(board, 'R' if ai_player == 'Y' else 'Y') or all(x != ' ' for x in board):  
    return evaluate_board(board, ai_player)

  if maximizing_player:
    # Find the move with the highest score for the AI
    best_score = -float('inf')
    for i, cell in enumerate(board):
      if cell == ' ' and (i>=35 or board[i+7]!=' '):
        board[i] = ai_player
        score = minimax(board, depth - 1, ai_player, False)  # Simulate opponent's move
        board[i] = ' '  # Backtrack
        best_score = max(best_score, score)
    return best_score
  else:
    # Find the move with the lowest score for the human player (maximize for AI)
    best_score = float('inf')
    for i, cell in enumerate(board):
      if cell == ' ' and (i>=35 or board[i+7]!=' '):
        board[i] = 'R' if ai_player == 'Y' else 'Y'  # Simulate human's move
        score = minimax(board, depth - 1, ai_player, True)  # AI's turn next
        board[i] = ' '  # Backtrack
        best_score = min(best_score, score)
    return best_score
  

def get_ai_move(board, ai_player, depth):
  """method to get the best move for the ai"""

  # Initialize best score and best move
  best_score = -float('inf')
  best_move = None

  # Iterate through all empty cells on the board
  for i, cell in enumerate(board):
    if cell == ' ' and (i>=35 or board[i+7]!=' '):
      # Simulate AI's move by placing its marker on the empty cell
      board[i] = ai_player
      score = minimax(board, depth - 1, ai_player, False)  # Simulate human's move
      board[i] = ' '  # Backtrack

      # Update best score and best move if this move leads to a better outcome for AI
      if score > best_score:
        best_score = score
        best_move = i
  return best_move  


if __name__ == "__main__":
  main()
