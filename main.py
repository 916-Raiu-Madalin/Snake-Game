from grid.grid import Grid
from ui.console import Ui

if __name__== "__main__":
    file=[]
    with open("settings.txt") as f:
        for line in f:
            tokens=line.split("=")
            file.append(tokens)

    dimension = int(file[0][1])
    apple_counter = int(file[1][1])

    grid = Grid(dimension,apple_counter)
    ui = Ui(dimension,apple_counter,grid)
    ui.start()
