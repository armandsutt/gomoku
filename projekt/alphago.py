from copy import deepcopy

class AlphaGo:
    
    def __init__(self):
        
        self.dict = {}
        self.dict["aaaaa"] = 10**100
        open_four = [" aaaa ", "a aaa a", "aa aa aa", "aaa a aaa"]
        for four in open_four:
            self.dict[four] = 10**10
        self.closed_four = self.blast(["aaaaa"])
        for four in self.closed_four:
            self.dict[four] = 10000
        self.open_three = self.blast(open_four)
        for three in self.open_three:
            self.dict[three] = 500
        closed_three = self.blast(self.closed_four)
        for three in closed_three:
            self.dict[three] = 100
        open_two = self.blast(self.open_three)
        for two in open_two:
            self.dict[two] = 50
        closed_two = self.blast(closed_three)
        for two in closed_two:
            self.dict[two] = 10
        open_one = self.blast(open_two)
        for one in open_one:
            self.dict[one] = 5
        closed_one = self.blast(closed_two)
        for one in closed_one:
            self.dict[one] = 1

    def blast(self, list):
        newlist = []
        for str in list:
            for i in range(len(str)):
                if str[i] == "a":
                    newstring = str[:i] + " " + str[i+1:]
                    add = True
                    for string in list:
                        if newstring in string:
                            add = False
                    if add:
                        newlist.append(newstring)
        return set(newlist)

    def move(self, board, color):
        dict = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    board[i][j] = color
                    value = self.minimax(self.tree(board, color * -1, 0, color))
                    dict[(i, j)] = value
                    board[i][j] = 0
        keys = list(dict.keys())
        values = list(dict.values())
        return keys[values.index(max(values))]
    
    def tree(self, board, player, depth, eval):
        branch = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    board[i][j] = player
                    if depth == 0: 
                        branch.append(self.evaluate(self.create_lines(board, eval)))
                    else:
                        branch.append(self.tree(board, player * -1, depth - 1, eval))
                    board[i][j] = 0
        if len(branch) == 0:
            branch.append(0)
        return branch
                    
    
    def minimax(self, tree, depth = 0):
        for e in tree:
            if type(e) is list:
                tree[tree.index(e)] = self.minimax(e, depth + 1)
        if depth % 2 == 0:
            return min(tree)
        else:
            return max(tree)
    
    def create_lines(self, board, color):
        lines = []
        rows = len(board)
        symbols = [" ", "h", "h"]
        symbols[color] = "a"
        for i in range(rows):
                row, col, dd1, dd2, du1, du2 = "", "", "", "", "", ""
                for j in range(len(board[i])):
                    row += symbols[board[i][j]]
                    col += symbols[board[j][i]]
                    if i + j >= 0 and i + j < rows:
                        dd1 += symbols[board[i + j][j]]
                        du1 += symbols[board[rows - 1 - i - j][j]]
                        if i != 0:
                            dd2 += symbols[board[j][i + j]]
                            du2 += symbols[board[rows - 1 - j][i + j]]
                lines.extend((row, col, dd1, dd2, du1, du2))
        return lines
    
    def aify(self, str):
        new = ""
        for letter in str:
            if letter == "h":
                new += "a"
            else:
                new += letter
        return new
    
    def evaluate(self, lines):
        value = 0
        humanthreat = False
        aithreat = False
        for line in lines:
            for i in range(5, 10):
                for j in range(len(line) - i + 1):
                    subline = line[j:i+j]
                    if subline in self.dict.keys():
                        value += self.dict[subline]
                        if subline in self.open_three:
                            if aithreat:
                                value += 50000
                            else:
                                aithreat = True
                    if "a" not in subline and "h" in subline:
                        subline = self.aify(subline)
                        if subline in self.dict.keys():
                            value -= 0.75*self.dict[subline]
                            if subline in self.open_three:
                                if humanthreat:
                                    value -= 40000
                                else:
                                    humanthreat = True
        return value