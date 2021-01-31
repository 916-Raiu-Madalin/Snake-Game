class Ui:
    def __init__(self,dimension,apples,grid):
        self._dimension = dimension
        self._apples =apples
        self._grid=grid
    def start(self):
        self.show_grid(self._grid.get_grid())

        while True:
            cmd= input("Give a command: ")


    def show_grid(self, grids):
        grid = grids

        line = "+---"
        print(line*self._dimension)
        for y in range(len(grid)):
            line = ""
            for x in grid[y]:
                if x == ".":
                    line += "| . "
                elif x =="+":
                    line += "| + "
                elif x == "*":
                    line += "| * "
                else:
                    line += "|   "
            line +=  "|\n"
            for x in range(1,self._dimension):
                line += "+---"
            line += "+---"
            print(line)