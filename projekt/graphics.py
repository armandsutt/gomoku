import pygame, game_board
from math import*

class Graphics:

    def draw_grid(self, screen, game_board):
        
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        BLACK = (0,0,0)
        self.padding = 10
        rows = game_board.get_rows()
        self.spacing = int((screen_width - 2 * self.padding) / rows)
        
        for i in range(rows + 1):
            pygame.draw.line(screen, BLACK, (self.padding, self.padding + i * self.spacing),
                             (screen_width - self.padding, self.padding + i * self.spacing), 1)
            pygame.draw.line(screen, BLACK, (self.padding + i * self.spacing, self.padding),
                             (self.padding + i * self.spacing, screen_height - self.padding), 1)
            
            
    def draw_pieces(self, screen, game_board):
        board = game_board.get_board()
        radius = round(0.45 * self.spacing)
        pos_x = self.padding + int(0.5 * self.spacing)
        pos_y = self.padding + int(0.5 * self.spacing)
        for row in board:
            for col in row:
                if col == 1:
                    pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y), radius, 1)
                elif col == -1:
                    pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y), radius, 0)
                pos_x += self.spacing
            pos_x = self.padding + int(0.5 * self.spacing)
            pos_y += self.spacing

            
            
    def draw_menu(self, screen, dim_state = 0, gametype_state = 0, color_state = 0):
        
        font2 = pygame.font.SysFont('leelawadeeui', 150)
        created_by_font = pygame.font.SysFont('mongolianbaiti',20)
        created_by = created_by_font.render("Created by Armand and Reijo", True, (200,50,50))
        font = pygame.font.SysFont('calibri', 50)
        title = font2.render("Gomoku", True, (100,0,50))
        screen.blit(title, (10, 10))
        screen.blit(created_by, (350,590))
        
        if dim_state == 10:
            tencolor = (200,50,50)
            twentycolor = (100,0,50)
        else:
            tencolor = (100,0,50)
            twentycolor = (200,50,50)
            
        ten = font.render("10x10", True, tencolor)
        twenty = font.render("20x20", True, twentycolor)
        
        screen.blit(ten, (30, 280))
        ten_rect = ten.get_rect()
        ten_rect.x, ten_rect.y = (30, 280)
        if gametype_state==0:
            screen.blit(twenty, (30, 320))
            twenty_rect = twenty.get_rect()
            twenty_rect.x, twenty_rect.y = (30, 320)
            if twenty_rect.collidepoint(pygame.mouse.get_pos()) and dim_state == 10:
                twenty = font.render("20x20", True, (255,0,0))
                screen.blit(twenty,(30,320))
        
        if ten_rect.collidepoint(pygame.mouse.get_pos()) and dim_state != 10:
            ten = font.render("10x10", True, (255,0,0))
            screen.blit(ten, (30, 280))
            
        if gametype_state == 0:
            vs_human_color = (200,50,50)
            vs_ai_color = (100,0,50)
        else:
            vs_human_color = (100,0,50)
            vs_ai_color = (200,50,50)
            
        vs_human = font.render("vs human", True, vs_human_color)
        vs_ai = font.render("vs AI", True, vs_ai_color)
        
        screen.blit(vs_human, (230, 280))
        vs_human_rect = vs_human.get_rect()
        vs_human_rect.x, vs_human_rect.y = (230, 280)
        
        screen.blit(vs_ai, (230, 320))
        vs_ai_rect = vs_ai.get_rect()
        vs_ai_rect.x, vs_ai_rect.y = (230, 320)
        
        if vs_human_rect.collidepoint(pygame.mouse.get_pos()) and gametype_state != 0:
            vs_human = font.render("vs human", True, (255,0,0))
            screen.blit(vs_human, (230, 280))
        
        if vs_ai_rect.collidepoint(pygame.mouse.get_pos()) and gametype_state == 0:
            vs_ai = font.render("vs AI", True, (255,0,0))
            screen.blit(vs_ai, (230, 320))
        
        if gametype_state != 0:
            dim_state=10
            if gametype_state == 1:
                as_white_color = (200,50,50)
                as_black_color = (100,0,50)
            else:
                as_white_color = (100,0,50)
                as_black_color = (200,50,50)
            
                
            as_white = font.render("as white", True, as_white_color)
            as_black = font.render("as black", True, as_black_color)
            
            screen.blit(as_white, (430, 280))
            as_white_rect = as_white.get_rect()
            as_white_rect.x, as_white_rect.y = (430, 280)
            
            screen.blit(as_black, (430, 320))
            as_black_rect = as_black.get_rect()
            as_black_rect.x, as_black_rect.y = (430, 320)
            
            if as_white_rect.collidepoint(pygame.mouse.get_pos()) and gametype_state != 1:
                as_white = font.render("as white", True, (255,0,0))
                screen.blit(as_white, (430, 280))
            
            if as_black_rect.collidepoint(pygame.mouse.get_pos()) and gametype_state != -1:
                as_black = font.render("as black", True, (255,0,0))
                screen.blit(as_black, (430, 320))
                
        start = font.render("Start!", True, (0,0,0))
        start_rect = start.get_rect()
        start_rect.x, start_rect.y = (260, 480)
        screen.blit(start, (260, 480))
        
        if start_rect.collidepoint(pygame.mouse.get_pos()):
            start = font.render("Start!", True, (255,0,0))
            screen.blit(start, (260, 480))
        
    
    def click(self, position):
        if position[0] > self.padding and position[1] > self.padding:
            col = int((position[0] - self.padding) // self.spacing)
            row = int((position[1] - self.padding) // self.spacing)
            return (row, col)
        return (-1,-1)
    
    def menu_click(self, mouse, dim, gametype):
        start = False
        if round(mouse[0]) in range(30,128) and round(mouse[1]) in range(280, 315):
            dim = 10
        if round(mouse[0]) in range(30,138) and round(mouse[1]) in range(320, 355) and gametype==0:
            dim = 20
        if round(mouse[0]) in range(230,393) and round(mouse[1]) in range(280, 315):
            gametype = 0
        if round(mouse[0]) in range(230,313) and round(mouse[1]) in range(320, 355):
            gametype = 1
            dim=10
        if round(mouse[0]) in range(430,568) and round(mouse[1]) in range(280, 315) and gametype != 0:
            gametype = 1
        if round(mouse[0]) in range(430,566) and round(mouse[1]) in range(320, 355) and gametype != 0:
            gametype = -1
        if round(mouse[0]) in range(260,350) and round(mouse[1]) in range(480, 525):
            start = True
        return start, dim, gametype
    
    def highlight_winner(self, screen, winning_line):
        for i in winning_line:
            pos_x = self.padding + self.spacing*i[1]
            pos_y = self.padding + self.spacing*i[0]
            pygame.draw.rect(screen, (0,255,0), [pos_x,pos_y, self.spacing, self.spacing],2)
            
    
    def hover_square(self, screen, game_board, player):
        mouseposition = pygame.mouse.get_pos()
        board = game_board.get_board()
        radius = int(self.spacing*0.45)
        pos_x = mouseposition[0] - (mouseposition[0] - self.padding) % self.spacing
        pos_y = mouseposition[1] - (mouseposition[1] - self.padding) % self.spacing
        square = pygame.draw.rect(screen, (255,255,255), [pos_x+1, pos_y+1 ,self.spacing-2, self.spacing-2])
        col = int((pos_x - self.padding) // self.spacing)
        row = int((pos_y - self.padding) // self.spacing)
        if square.collidepoint(mouseposition):
            if row >= 0 and row < len(board) and col >= 0 and col < len(board):
                if board[row][col] == 0:
                    if player == 1:
                        pygame.draw.circle(screen, (0,0,0), ((pos_x+int(self.spacing*0.5), pos_y+int(self.spacing*0.5))), radius, 1)
                    else:
                        pygame.draw.circle(screen, (0,0,0), ((pos_x+int(self.spacing*0.5), pos_y+int(self.spacing*0.5))), radius, 0)
                        
    def highlight_last_move(self, screen, last_move):
        if last_move is None:
            return None
        pos_x = self.padding + self.spacing * last_move[1]
        pos_y = self.padding + self.spacing * last_move[0]
        pygame.draw.rect(screen, (255, 0, 0), [pos_x, pos_y, self.spacing + 1, self.spacing + 1], 1)
            
        
            
        