# Setting the game display
import pygame
import sys
import time

# Initializing Pygame
pygame.init()

# Constraints
WINDOW_SIZE = 300
GRID_SIZE = 100
LINE_WIDTH = 5

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = ( 0, 0, 0)

#Set up the display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Tic Tac Toe')

# Setting up the game state
game_board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))

# Drawing game elements
def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * GRID_SIZE, 0), (i * GRID_SIZE, WINDOW_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * GRID_SIZE), (WINDOW_SIZE, i * GRID_SIZE), LINE_WIDTH)

def draw_x(row, col):
    offset = GRID_SIZE // 4
    pygame.draw.line(screen, LINE_COLOR, (col * GRID_SIZE + offset, row * GRID_SIZE + offset),
                     ((col + 1) * GRID_SIZE - offset, (row + 1) * GRID_SIZE - offset), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, ((col + 1) * GRID_SIZE - offset, row * GRID_SIZE + offset),
                     (col * GRID_SIZE + offset, (row + 1) * GRID_SIZE - offset), LINE_WIDTH)

def draw_o(row, col):
    offset = GRID_SIZE // 4
    pygame.draw.circle(screen, LINE_COLOR, (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2),
                       GRID_SIZE // 2 - offset, LINE_WIDTH)
    
def show_message(message):
    font = pygame.font.SysFont(None, 30)
    text = font.render(message, True, LINE_COLOR)
    screen.blit(text, (10, WINDOW_SIZE // 2))

# Main game loop
running  = True
game_over = False

while running:
    screen.fill(WHITE)
    draw_lines()

    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            running = False
            sys.exit()
        
        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // GRID_SIZE, x // GRID_SIZE

            if game_board[row][col] == ' ':
                game_board[row][col] = current_player

                if check_win(game_board, current_player):
                    print(f"Player {current_player} Wins !!")
                    game_over = True
                elif check_draw(game_board):
                    message = "It's a draw!"
                    show_message(message)
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
    
    # Draw symbols
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == 'X':
                draw_x(row, col)
            elif game_board[row][col] == 'O':
                draw_o(row, col)
    
    pygame.display.flip()
    pygame.time.delay(100) # Adding a delay to slow down game after its over

pygame.quit()
sys.exit()
