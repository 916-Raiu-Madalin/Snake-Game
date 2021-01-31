class Ui:
    def __init__(self,dimension,apples,grid):
        self._dimension = dimension
        self._apples =apples
        self._grid=grid
        self.direction='up'
    def start(self):
        self.show_grid(self._grid.get_grid())

        commands={'move':self.ui_move,'up':self.ui_directions,'down':self.ui_directions,'left':self.ui_directions,'right':self.ui_directions}
        try:
            while True:
                cmd= input("Give a command: ")
                if cmd=='exit':
                    print("Bye")
                    break
                cmd,args = self.get_commands_arguments(cmd)
                if cmd == "move":
                    try:
                        if len(args)>0:
                            commands[cmd](int(args[0]))
                        else:
                            commands[cmd](1)
                    except ValueError as ve:
                        print("You need to put a valid int after move")
                elif cmd == "up":
                    commands[cmd](cmd)
                elif cmd == "down":
                    commands[cmd](cmd)
                elif cmd == "right":
                    commands[cmd](cmd)
                elif cmd == "left":
                    commands[cmd](cmd)
                else:
                    print("Wrong command :D")
        except Exception as e:
            print(e)
    def get_commands_arguments(self,cmd_line):
        """
        :param cmd_line:the command with the arguments
        :return: the command and the arguments separated
        """
        pos = cmd_line.find(" ")
        if pos == -1:  # no arguments were found
            return cmd_line, []
        cmd = cmd_line[:pos]

        args = cmd_line[pos + 1:]
        args = args.split(' ')
        args = [s.strip() for s in args]
        return cmd, args

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
    def ui_move(self,number):
        self._grid.move(number,self.direction)
        self.show_grid(self._grid.get_grid())


    def ui_directions(self,direction):
        if self.direction =="up" and direction =="down" or self.direction =="down" and direction == "up":
            print("You cannot make a 180 degree move, try another direction")
            return
        elif self.direction =="left" and direction =="right" or self.direction =="right" and direction == "left":
            print("You cannot make a 180 degree move, try another direction")
            return

        self.direction = direction
        self.ui_move(1)
