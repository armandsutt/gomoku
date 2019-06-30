import sys, pygame, game_board, graphics, time, alphago

WHITE = (255,255,255)
SIZE = (620, 620)
GOLD = (255,225,0)

pygame.init()
screen = pygame.display.set_mode(SIZE)

white_win_image = pygame.image.load("white_win_image.png")
black_win_image = pygame.image.load("black_win_image.png")
tie_image = pygame.image.load("tie_image.png")
icon = pygame.image.load("icon.png")

pygame.display.set_caption("Gomoku")
pygame.display.set_icon(icon)

graph = graphics.Graphics()
alphago = alphago.AlphaGo()

while True:
    screen.fill(WHITE)
    pygame.display.update()
    
    start_game = False
    dim = 10
    gametype = 0
    while not start_game:
        screen.fill(GOLD)
        graph.draw_menu(screen, dim, gametype)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_game, dim, gametype = graph.menu_click(event.pos, dim, gametype)
        pygame.display.update()

    screen.fill(WHITE)
    board = game_board.GameBoard(dim, dim)
    graph.draw_grid(screen, board)
    pygame.display.update()
    
    gametype *= -1
    winner = 0
    player = 1
    move_coords = None
    while winner == 0:
        if gametype == player:
            move_coords = alphago.move(board.get_board(), player)
            move = board.move(move_coords, player)
            if move:
                player *= -1
            winner = board.check_winner()
            graph.draw_pieces(screen, board)
            pygame.display.update()
        if winner != 0:
            break
        screen.fill(WHITE)
        graph.draw_grid(screen, board)
        if gametype != 0:
            graph.highlight_last_move(screen, move_coords)
        graph.hover_square(screen, board, player)
        graph.draw_pieces(screen, board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                move_coords = graph.click(event.pos)
                move = board.move(move_coords, player)
                if move:
                    player *= -1
                winner = board.check_winner()
                graph.draw_pieces(screen, board)
                pygame.display.update()
    if winner != 2:
        graph.highlight_winner(screen, board.get_winning_line(move_coords))
        pygame.display.update()
    time.sleep(3)
    if winner == -1:
        screen.blit(black_win_image,(0,0))
    elif winner == 1:
        screen.blit(white_win_image,(0,0))
    else:
        screen.blit(tie_image, (0,0))
    pygame.display.update()

    new_game = False
    while not new_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    new_game = True
