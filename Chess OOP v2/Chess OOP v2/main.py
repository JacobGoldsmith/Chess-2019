'''
Max is a silly billy
Objective:

'''

from pieces_classes import piece
from queen import queen
from rook import rook
from bishop import bishop
from knight import knight
from set_up_board import set_up
from user_move import user_move
from next_turn import next_turn
from aimove import aimove
from undo_move import undo_move
from print_board import print_board
from update_board import update_board
from game import possible_move_highlight, draw_board, update_board_draw, update_board_for_drag
from choose_promotion import choose_promotion
from board_obj import board_obj
import sys
import math
import pygame
pygame.init()


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

#INITIALIZING
pieces_on_the_board = []
list_of_pieces_moved = []
boardobject = board_obj(pieces_on_the_board)
set_up(boardobject, pieces_on_the_board)

myfont = pygame.font.SysFont("comicsansms", 70)
myfont1 = pygame.font.SysFont("comicsansms", 20)
white_color=(200,173,127)
black_color=(131,105,83)
circle_color = (200, 200, 200) #('#dcf0ef')
square_size = 50
width = 8*square_size
height = 8*square_size 
drag_sound = pygame.mixer.Sound('drag_sound.wav')
move_sound = pygame.mixer.Sound('move_sound.wav')

#board= [['_' for i in range(8)] for j in range(8)] # not sure i need this

screen = pygame.display.set_mode((width, height))
draw_board(screen, white_color, black_color, square_size)
pygame.display.update()

turn = 'white'

click_track = 1
print("what piece would you like to move?")
#UPDATING THE PIECES ON THE BOARD
#board = update_board(pieces_on_the_board, board) #MAYBE NOT NEED
#PRINTING THE BOARD
update_board_draw(boardobject, screen, square_size, white_color, black_color) #ADAPT FOR NEW BOARD
pygame.display.update()
print_board(boardobject) #ADAPT FOR NEW BOARD

#EXECUTING MOVES
user_color = 'white'
#computer_color ='black'
computer_color ='not playing'
#user2_color ='not playing'
user2_color ='black'

click_track = 1
running = True
dragging = False
while running:
    if turn == computer_color:
        result = aimove(boardobject, pieces_on_the_board, list_of_pieces_moved, turn)
        #UPDATING AND PRINTING THE COMMAND LINE BOARD
        if result == True:
            turn = next_turn(turn)
            print_board(boardobject)
            #UPDATING AND PRINTING THE PYGAME BOARD
            update_board_draw(boardobject, screen, square_size, white_color, black_color)
            pygame.display.update()
            drag_sound.play()
        if result == 'stalemate':
            running = False
            board = update_board(pieces_on_the_board, board)
            update_board_draw(boardobject, screen, square_size, white_color, black_color)
            print_board(boardobject)
            label=myfont.render("stalemate!", 1, (0,255,0))
            screen.blit(label, (40,10))
            pygame.display.update()
            pygame.time.wait(5000)
            sys.exit()
            break
        if result == 'checkmate':
            running = False
            board = update_board(pieces_on_the_board, board)
            update_board_draw(boardobject, screen, square_size, white_color, black_color)
            print_board(boardobject)
            label=myfont.render("Checkmate!", 1, (0,255,0))
            screen.blit(label, (40,10))
            pygame.display.update()
            pygame.time.wait(5000)
            sys.exit()
            break
    if turn == user_color or turn == user2_color:      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    res = undo_move(boardobject, pieces_on_the_board, list_of_pieces_moved) #NEED TO UPDATE
                    if res:
                        turn = next_turn(turn)
                    #PRINTING THE BOARD
                    update_board_draw(boardobject, screen, square_size, white_color, black_color)
                    pygame.display.update()
                    print_board(boardobject)
               
            if event.type == pygame.MOUSEBUTTONDOWN:
                if click_track == 2:
                    break
                else:
                    dragging = True
                    source = [int(math.floor(event.pos[0]/square_size)), int(math.floor(event.pos[1]/square_size))]
                    dragging_piece = boardobject.squares[source[0]][source[1]].piece # find_piece(pieces_on_the_board, source[0], source[1]) 
            if event.type == pygame.MOUSEBUTTONUP:
                print("mousebuttonup 101 main")
                if click_track == 2:
                    k, l = [int(math.floor(event.pos[0]/square_size)), int(math.floor(event.pos[1]/square_size))]
                    click_track = 3   
                else:
                    dragging = False
                    dest = [int(math.floor(event.pos[0]/square_size)), int(math.floor(event.pos[1]/square_size))]
                    i, j = source
                    piece = boardobject.squares[j][i].piece
                    if piece:
                        possible_move_highlight(boardobject, piece.possible_destinations, screen, square_size, circle_color)
                        pygame.display.update()
                    if source == dest:
                        click_track = 2
                    else:
                        k, l = dest
                        click_track = 3

            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    dragging_coordinates = [int(event.pos[0]/square_size), int(event.pos[1]/square_size)]
                    update_board_draw(boardobject, screen, square_size, white_color, black_color)
                    update_board_for_drag(boardobject, source[0], source[1], dragging_piece, \
                    dragging_coordinates[0], dragging_coordinates[1], boardobject, screen, square_size, white_color, black_color, circle_color)
                    pygame.display.update()

            if click_track == 3:
                click_track = 1
                result = user_move(boardobject, pieces_on_the_board, list_of_pieces_moved, turn, i, j, k, l, screen)
                if result == True:
                    turn = next_turn(turn)
                    move_sound.play()
                    for piece in pieces_on_the_board:
                        print(piece.name, piece.possible_destinations)
                    print("board takes this many bytes", get_size(boardobject))
                    print_board(boardobject)
                if result == False:
                    print ("try again 128 main")
                #PRINTING THE BOARD
                update_board_draw(boardobject, screen, square_size, white_color, black_color)
                pygame.display.update()
                if result == 'stalemate':
                    update_board_draw(boardobject, screen, square_size, white_color, black_color)
                    print_board(boardobject)
                    label=myfont.render("stalemate!", 1, (0,255,0))
                    screen.blit(label, (40,10))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    sys.exit()
                    break
                if result == 'checkmate':
                    update_board_draw(boardobject, screen, square_size, white_color, black_color)
                    print_board(boardobject)
                    label=myfont.render("Checkmate!", 1, (0,255,0))
                    screen.blit(label, (40,10))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    sys.exit()
                    break

                print (turn, "main  219")
                # for piece in pieces_on_the_board:
                #     print (piece.color, piece, piece.location[-1])
                #     print (piece.possible_destinations)
