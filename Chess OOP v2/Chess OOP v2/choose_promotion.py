def choose_promotion(name, k, l):
    from queen import queen
    from rook import rook
    from bishop import bishop
    from knight import knight
    import sys
    import pygame
    pygame.init()
    if name.islower():
        color = 'black'
    if name.isupper():
        color = 'white'
#    width = 500
#    height = 200
#    screen2 = pygame.display.set_mode((width, height))
    myfont = pygame.font.SysFont("monospace", 20)
    label1=myfont.render("Please choose your pawn promotion", 1, (0,255,0))
    label2=myfont.render("q, r, b, n", 1, (0,255,0))
    screen.blit(label1, (40,10))
    screen.blit(label2, (180, 40))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return queen(color, k, l)
                if event.key == pygame.K_r:
                    return rook(color, k, l)
                if event.key == pygame.K_b:
                    return bishop(color, k, l)
                if event.key == pygame.K_n:
                    return knight(color, k, l)
