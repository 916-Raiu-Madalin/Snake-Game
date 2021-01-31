from random import randint


class Grid:
    def __init__(self, dimension, apples):
        self.grid = []
        self._dimension = dimension
        self._apples = apples
        for y in range(0, dimension):
            row = []
            for x in range(0, dimension):
                row.append("")
            self.grid.append(row)

        self.grid[self._dimension // 2 - 1][self._dimension // 2] = '*'
        self.grid[self._dimension // 2][self._dimension // 2] = '+'
        self.grid[self._dimension // 2 + 1][self._dimension // 2] = '+'

        x = self._apples
        while x > 0:
            a = randint(0, self._dimension - 1)
            b = randint(0, self._dimension - 1)
            if self.grid[a][b] == "":
                if a > 0 and a < (self._dimension - 1) and b > 0 and b < (self._dimension - 1):
                    if self.grid[a + 1][b] != "." and self.grid[a][b + 1] != "." and self.grid[a - 1][b] != "." and \
                            self.grid[a][b - 1] != ".":
                        self.grid[a][b] = '.'
                        x -= 1
                if a == 0 and b > 0 and self.grid[a][b] == "" and b < (self._dimension - 1):
                    if self.grid[a + 1][b] != "." and self.grid[a][b + 1] != "." and self.grid[a][b - 1]:
                        self.grid[a][b] = '.'
                        x -= 1
                elif a == self._dimension - 1 and b > 0 and self.grid[a][b] == "" and b < (self._dimension - 1):
                    if self.grid[a - 1][b] != "." and self.grid[a][b - 1] != "." and self.grid[a][b + 1]:
                        self.grid[a][b] = '.'
                        x -= 1
                elif a == self._dimension - 1 and b == 0 and self.grid[a][b] == "":
                    if self.grid[a - 1][b] != "." and self.grid[a][b + 1] != ".":
                        self.grid[a][b] = '.'
                        x -= 1
                elif a == self._dimension - 1 and b == self._dimension - 1 and self.grid[a][b] == "":
                    if self.grid[a - 1][b] != "." and self.grid[a][b - 1] != ".":
                        self.grid[a][b] = '.'
                        x -= 1
                elif a > 0 and a < self._dimension - 1 and b == 0:
                    if self.grid[a - 1][b] != "." and self.grid[a][b + 1] != "." and self.grid[a + 1][b]:
                        self.grid[a][b] = '.'
                        x -= 1
                elif a > 0 and a < self._dimension - 1 and b == self._dimension - 1:
                    if self.grid[a - 1][b] != "." and self.grid[a][b + -1] != "." and self.grid[a + 1][b]:
                        self.grid[a][b] = '.'
                        x -= 1


    def get_grid(self):
        return self.grid

    def get_position(self):
        for i in range(0, self._dimension):
            for j in range(0, self._dimension):
                if self.grid[i][j] == "*":
                    return i, j

    def move(self, number, direction):
        i, j = self.get_position()
        if direction == "up":
            if i - number < 0:
                raise Exception("Game over!")
        if direction == "down":
            if i + number > self._dimension - 1:
                raise Exception("Game over!")
        if direction == "right":
            if j + number > self._dimension - 1:
                raise Exception("Game over!")
        if direction == "left":
            if j - number < 0:
                raise Exception("Game over!")

        if direction == "up":
            for x in range(0, number):
                if self.grid[i - 1][j] == ".":
                    self.grid[i - 1][j] = self.grid[i][j]
                    self.grid[i][j] = "+"
                    i -= 1
                    print("da")
                else:
                    self.check_game_over(i - 1, j)
                    self.grid[i - 1][j] = self.grid[i][j]
                    self.grid[i][j] = "+"
                    i -= 1

                    self.move_snake_tail()

        elif direction == "down":
            for x in range(0, number):
                if self.grid[i + 1][j] == ".":
                    self.grid[i + 1][j] = self.grid[i][j]
                    self.grid[i][j] = "+"
                    i += 1

                else:
                    self.check_game_over(i + 1, j)
                    self.grid[i + 1][j] = self.grid[i][j]
                    self.grid[i][j] = "+"
                    i += 1
                    self.move_snake_tail()

        elif direction == "left":
            for x in range(0, number):
                if self.grid[i][j - 1] == ".":
                    self.grid[i][j - 1] = self.grid[i][j]
                    self.grid[i][j] = "+"
                    i += 1
                else:
                    self.check_game_over(i, j - 1)
                    self.grid[i][j - 1] = self.grid[i][j]
                    self.grid[i][j] = "+"
                    i += 1
                    self.move_snake_tail()
        elif direction == "right":
            for x in range(0, number):
                if self.grid[i][j + 1] == ".":
                    self.grid[i][j + 1] = self.grid[i][j]
                    self.grid[i][j] = "+"
                    i += 1
                else:
                    self.check_game_over(i, j + 1)
                    self.grid[i][j + 1] = self.grid[i][j]
                    self.grid[i][j] = "+"
                    i += 1
                    self.move_snake_tail()
    def move_snake_tail(self):
        pass

    def check_game_over(self, i, j):
        if self.grid[i][j] == "+":
            raise Exception("Game over! You hit yourself")
