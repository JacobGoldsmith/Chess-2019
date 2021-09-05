import pygame
import sys
import os
pygame.init()

mypath = os.path.dirname(os.path.dirname(os.path.dirname( os.path.realpath( __file__ ) )))

black_rook = pygame.image.load( os.path.join(mypath, 'black_rook.png'))
black_queen = pygame.image.load( os.path.join(mypath, 'black_queen.png'))
black_knight = pygame.image.load( os.path.join(mypath, 'black_knight.png'))
black_bishop = pygame.image.load( os.path.join(mypath, 'black_bishop.png'))
black_king = pygame.image.load( os.path.join(mypath, 'black_king.png'))
black_pawn = pygame.image.load( os.path.join(mypath, 'black_pawn.png'))
white_king = pygame.image.load( os.path.join(mypath, 'white_king.png'))
white_queen = pygame.image.load( os.path.join(mypath, 'white_queen.png'))
white_knight = pygame.image.load( os.path.join(mypath, 'white_knight.png'))
white_bishop = pygame.image.load( os.path.join(mypath, 'white_bishop.png'))
white_rook = pygame.image.load( os.path.join(mypath, 'white_rook.png'))
white_pawn = pygame.image.load( os.path.join(mypath, 'white_pawn.png'))


def draw_board(screen, white_color, black_color, square_size):
    for r in range(8):
        for c in range(8):
                if (c+r)%2==0:
                    pygame.draw.rect(screen, white_color, (c*square_size, r*square_size, square_size, square_size), 0)
                if (c+r)%2==1:
                    pygame.draw.rect(screen, black_color, (c*square_size, r*square_size, square_size, square_size), 0)

def update_board_draw(board_obj, screen, square_size, white_color, black_color):
    for r in range(8):
        for c in range(8):
            if (c+r)%2==0:
                pygame.draw.rect(screen, white_color, (c*square_size, r*square_size, square_size, square_size), 0)
            if (c+r)%2==1:
                pygame.draw.rect(screen, black_color, (c*square_size, r*square_size, square_size, square_size), 0)
            if board_obj.squares[r][c].piece == None:
                continue
            if board_obj.squares[r][c].piece.name == 'r':
                screen.blit(black_rook, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'q':
                screen.blit(black_queen, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'k':
                screen.blit(black_king, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'n':
                screen.blit(black_knight, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'b':
                screen.blit(black_bishop, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'p':
                screen.blit(black_pawn, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'B':
                screen.blit(white_bishop, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'K':
                screen.blit(white_king, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'N':
                screen.blit(white_knight, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'Q':
                screen.blit(white_queen, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'P':
                screen.blit(white_pawn, (c*square_size-7, r*square_size-6))
            if board_obj.squares[r][c].piece.name == 'R':
                screen.blit(white_rook, (c*square_size-7, r*square_size-6))

def update_board_for_drag(board_obj, c, r, piece, x, y, board, screen, square_size, white_color, black_color, circle_color):
    if (c+r)%2==0:
        pygame.draw.rect(screen, white_color, (c*square_size, r*square_size, square_size, square_size), 0)
    if (c+r)%2==1:
        pygame.draw.rect(screen, black_color, (c*square_size, r*square_size, square_size, square_size), 0)
    if board_obj.squares[r][c].piece == None:
        return
    if board_obj.squares[r][c].piece.name == 'r':
        screen.blit(black_rook, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'q':
        screen.blit(black_queen, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'k':
        screen.blit(black_king, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'n':
        screen.blit(black_knight, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'b':
        screen.blit(black_bishop, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'p':
        screen.blit(black_pawn, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'B':
        screen.blit(white_bishop, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'K':
        screen.blit(white_king, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'N':
        screen.blit(white_knight, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'Q':
        screen.blit(white_queen, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'P':
        screen.blit(white_pawn, (x*square_size-7, y*square_size-6))
    if board_obj.squares[r][c].piece.name == 'R':
        screen.blit(white_rook, (x*square_size-7, y*square_size-6))
    for coord in board_obj.squares[r][c].piece.possible_destinations:
        pygame.draw.circle(screen, circle_color, [coord[1]*square_size+23, coord[0]*square_size+27], 10)
    
def possible_move_highlight(board_obj, list_of_coordinates, screen, square_size, circle_color):
    for coord in list_of_coordinates:
        pygame.draw.circle(screen, circle_color, [coord[1]*square_size+23, coord[0]*square_size+27], 10)