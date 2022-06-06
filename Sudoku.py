class Sudoku:

    def __init__(self,board=None):
        if board is None:
            self.board = [[None]*9]*9
        else:
            self.parse(board)
    
    def parse(self,board):
        board = board.split('\n')

        def process_char(c):
            try:
                if int(c) in {1,2,3,4,5,6,7,8,9}:
                    return int(c)
                else:
                    return None
            except:
                return None
        
        self.board = []

        for line in board:
            self.board.append([process_char(c) for c in line])
    
    def __repr__(self):
        out_string=''
        for line in self.board:
            for c in line:
                if c is not None:
                    out_string += str(c)
                else:
                    out_string+="."
            out_string+="\n"
        return out_string

    def poss(self,i,j):
        poss_set={1,2,3,4,5,6,7,8,9}
        poss_set-=set(self.board[j])
        poss_set-=set([self.board[k][i]for k in range(9)])
        
        box_i = 3*(i // 3)
        box_j = 3*(j // 3)
        for k in range(3):
            poss_set -= set(self.board[box_j+k][box_i:box_i+3])
        return poss_set
       
    def reduce_1_poss(self):
        for i in range(9):
            for j in range(9):
                if self.board[j][i] is None:
                    square_poss = self.poss(i,j)
                    if len(square_poss) == 1:
                        self.board[j][i] = list(square_poss)[0]
                        self.changed = True

    def reduce_row_poss(self):
        for i in range(9):
            row_poss=[self.poss(i,j) for j in range(9)]
            for digit in range(1,10):
                poss_cells=[k for k, square in enumerate(row_poss) if digit in square]
                if len(poss_cells) == 1 and self.board[poss_cells[0]][i] is None:
                    self.board[poss_cells[0]][i] = digit
                    self.changed=True
    
    '''def reduce_col_poss(self):
        for i in range(9):
            col_poss=[self.poss(j,i) for j in range(9)]
            for digit in range(1,10):
                poss_cells=[k for k, square in enumerate(col_poss) if digit in square]
                if len(poss_cells) == 1 and self.board[poss_cells[0]][i] is None:
                    self.board[poss_cells[0]][i] = digit
                    self.changed=True'''
    def guess(self):
        new_board=self.board

        
        guess_slot = [0,0,9]
        for row in range(9):
            for col in range(9):
                pos_poss = poss(new_board[row][col])
                if len(pos_poss) == 2:
                    guess_slot = [row,col,pos_poss]
                    break
                elif len(pos_poss) > len(guess_slot[2]):
                    guess_slot = [row,col,pos_poss]

                    
    
    def solve(self):
        while True:
            self.changed = False
            self.reduce_1_poss()
            self.reduce_row_poss()
            if not self.changed:
                break
        
        #self.guess()


def main():
    board = \
        """5.8.1.4.7
34....9..
1........
.73.9125.
8.17.6.4.
92...5.71
.854.....
.195..7..
734...598"""
    test_board=Sudoku(board)
    print(test_board)
    test_board.solve()
    print(test_board)

if __name__ == '__main__':
    main()