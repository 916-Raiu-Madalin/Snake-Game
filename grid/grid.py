from random import randint


class Grid:
    def __init__(self,dimension,apples):
        self.grid = []
        self._dimension= dimension
        self._apples = apples
        for y in range(0, dimension):
            row = []
            for x in range(0, dimension):
                row.append("")
            self.grid.append(row)
        self.grid[self._dimension//2 -1][self._dimension//2 ] ='*'
        self.grid[self._dimension//2 ][self._dimension//2 ] ='+'
        self.grid[self._dimension//2 +1][self._dimension//2 ] ='+'

        x = self._apples
        while x > 0:
            a= randint(0,self._dimension-1)
            b= randint(0,self._dimension-1)
            if self.grid[a][b] =="":
                if a>0 and a <(self._dimension-1) and b>0 and b <(self._dimension-1):
                    if self.grid[a+1][b] !="." and self.grid[a][b+1] !="." and self.grid[a-1][b] !="." and self.grid[a][b-1] !=".":
                        self.grid[a][b] = '.'
                        x -= 1
                if a == 0  and b >0 and self.grid[a][b] == "" and b <(self._dimension-1):
                    if self.grid[a+1][b]!="." and self.grid[a][b+1]!="." and self.grid[a][b-1]:
                        self.grid[a][b] = '.'
                        x -= 1
                elif a == self._dimension-1 and b >0 and self.grid[a][b] == "" and b <(self._dimension-1):
                    if self.grid[a-1][b]!="." and self.grid[a][b-1]!="." and self.grid[a][b+1]:
                        self.grid[a][b] = '.'
                        x -= 1
                elif a == self._dimension-1 and b == 0 and self.grid[a][b] == "":
                    if self.grid[a-1][b]!="." and self.grid[a][b+1]!=".":
                        self.grid[a][b] = '.'
                        x -= 1
                elif a == self._dimension-1 and b == self._dimension-1 and self.grid[a][b] == "":
                    if self.grid[a-1][b]!="." and self.grid[a][b-1]!=".":
                        self.grid[a][b] = '.'
                        x -= 1
                elif a>0 and a <self._dimension-1 and b == 0:
                    if self.grid[a-1][b]!="." and self.grid[a][b+1]!="." and self.grid[a+1][b]:
                        self.grid[a][b] = '.'
                        x -= 1
                elif a > 0 and a < self._dimension - 1 and b == self._dimension-1:
                    if self.grid[a-1][b]!="." and self.grid[a][b+-1]!="." and self.grid[a+1][b]:
                        self.grid[a][b] = '.'
                        x -= 1


    def get_grid(self):
        return self.grid