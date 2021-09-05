from is_on_board import is_on_board
from undo_move import undo_move
from in_check import in_check
from next_turn import next_turn
from checkmate import checkmate
from is_stalemate import is_stalemate
import time
import math
import pygame
from rook import rook
from bishop import bishop
from knight import knight
from queen import queen
pygame.init()
myfont1 = pygame.font.SysFont("comicsansms", 20)

def user_move(boardobject, pieces_on_the_board, list_of_pieces_moved, turn, a, b, c, d, screen):
    if is_stalemate(boardobject, pieces_on_the_board, list_of_pieces_moved, turn):
        return 'stalemate'
    i, j, k, l = b, a, d, c
    if is_on_board([i, j]) == False or is_on_board([k, l]) == False:
        return False 
    if boardobject.squares[i][j].piece == None:
        return False
    if boardobject.squares[i][j].piece.color!= turn:
        return False
    result = False
    result = boardobject.squares[i][j].piece.make_move(k, l, boardobject, pieces_on_the_board, list_of_pieces_moved, turn)    
    if result == 'promotion':
        label1=myfont1.render("Please choose your pawn promotion", 1, (0,255,0))
        label2=myfont1.render("q, r, b, n", 1, (0,255,0))
        screen.blit(label1, (40,10))
        screen.blit(label2, (180, 40))
        pygame.display.update()
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        promoted = queen(turn, k, l)
                        loop = False
                        break
                    if event.key == pygame.K_r:
                        promoted = rook(turn, k, l)
                        loop = False
                        break
                    if event.key == pygame.K_b:
                        promoted = bishop(turn, k, l)
                        loop = False
                        break
                    if event.key == pygame.K_n:
                        promoted = knight(turn, k, l)
                        loop = False
                        break
        pieces_on_the_board.append(promoted)
        pieces_on_the_board[-1].location.insert(0, 'off the board')
        list_of_pieces_moved[-1].insert(1, pieces_on_the_board[-1])
        a, b = pieces_on_the_board[-1].location[-1][0], pieces_on_the_board[-1].location[-1][1]
        boardobject.squares[a][b].piece = pieces_on_the_board[-1]
        boardobject.squares[a][b].piece.update_possible_destinations(boardobject, pieces_on_the_board)
        result = True
    return result