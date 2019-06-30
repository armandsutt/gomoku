class GameBoard:
    
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [[0 for j in range(columns)] for i in range(rows)]
    
    def get_board(self):
        return self.board
    
    def get_rows(self):
        return self.rows
    
    def get_columns(self):
        return self.columns
    
    def move(self, coords, player):
        row = coords[0]
        column = coords[1]
        if row in range(self.rows) and column in range(self.columns) and self.board[row][column] == 0:
            self.board[row][column] = player
            return True
        else:
            return False
        
    def check_winner(self):
        lines = []
        symbols = [" ", "w", "b"]
        for i in range(self.rows):
            row, col, dd1, dd2, du1, du2 = "", "", "", "", "", ""
            for j in range(self.columns):
                row += symbols[self.board[i][j]]
                col += symbols[self.board[j][i]]
                if i + j >= 0 and i + j < self.rows:
                    dd1 += symbols[self.board[i + j][j]]
                    du1 += symbols[self.board[self.rows - 1 - i - j][j]]
                    if i != 0:
                        dd2 += symbols[self.board[j][i + j]]
                        du2 += symbols[self.board[self.rows - 1 - j][i + j]]
            lines.extend((row, col, dd1, dd2, du1, du2))
        for line in lines:
            if "wwwww" in line:
                return 1
            if "bbbbb" in line:
                return -1
        tie = True
        for row in self.board:
            if 0 in row:
                tie = False
        if tie:
            return 2
        return 0
    
    def get_winning_line(self, last_move):
        row = last_move[0]
        col = last_move[1]
        player = self.board[row][col]
        endsquare = None
        #check row
        rowcounter = 0
        colcounter = 0
        d1counter = 0
        d2counter = 0
        cexists = False
        rexists = False
        for i in range(-4, 5):
            if col + i >= 0 and col + i < len(self.board):
                cexists = True
                if self.board[row][col+i] == player:
                    rowcounter += 1
                    if rowcounter == 5:
                        endsquare = ("r", (row, col+i))
                        break
                else:
                    rowcounter = 0
            else:
                cexists = False
            if row + i >= 0 and row + i < len(self.board):
                rexists = True
                if self.board[row + i][col] == player:
                    colcounter += 1
                    if colcounter == 5:
                        endsquare = ("c", (row + i, col))
                        break
                else:
                    colcounter = 0
            else:
                rexists = False
            if rexists and cexists:
                if self.board[row + i][col + i] == player:
                    d1counter += 1
                    if d1counter == 5:
                        endsquare = ("d1", (row + i, col + i))
                        break
                else:
                    d1counter = 0
            if cexists and row - i >= 0 and row - i < len(self.board):
                if self.board[row - i][col + i] == player:
                    d2counter += 1
                    if d2counter == 5:
                        endsquare = ("d2", (row - i, col + i))
                        break
                else:
                    d2counter = 0
        if endsquare[0] == "r":
            pos = endsquare[1][1]
            return [(row, x) for x in range(pos - 4, pos + 1)]
        elif endsquare[0] == "c":
            pos = endsquare[1][0]
            return [(x, col) for x in range(pos - 4, pos + 1)]
        elif endsquare[0] == "d1":
            r = endsquare[1][0]
            c = endsquare[1][1]
            return [(r + x, c + x) for x in range(-4, 1)]
        else:
            r = endsquare[1][0]
            c = endsquare[1][1]
            return [(r - x, c + x) for x in range(-4,1)]
        