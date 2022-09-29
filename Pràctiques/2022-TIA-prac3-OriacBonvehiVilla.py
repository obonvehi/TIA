class JocDelOs:
    @staticmethod
    def main(args):
        JocDelOs(3)

    size = 0
    board = None
    o_wins = 0
    s_wins = 0
    tables = 0
    sc = "Python-inputs"

    def __init__(self, size):
        self.size = 3
        self.board = [['-'] * (self.size) for _ in range(self.size)]
        self.play()

    def play(self):
        i = self.selectModeGame()
        if i == 1:
            self.oneMinimax()
        elif i == 2:
            self.twoMinimax()

    def twoMinimax(self):
        turn = 0
        points = 0
        while turn < 9:
            self.o_wins = 0
            self.s_wins = 0
            self.tables = 0
            print("\n----------------TORN DEL JUGADOR 1 (MINIMAX)----------------")
            n2 = self.minimax(turn, points, True)
            self.board[n2.x][n2.y] = 'O'
            points = n2.points
            turn += 1
            self.printMinimaxNodes(n2, turn)
            self.printBoard()
            print("Probabilitat de victoria Jugador O:" + "  " + str(
                1 / (self.o_wins + self.s_wins + self.tables) * self.o_wins))
            print("Probabilitat de victoria Jugador S:" + "  " + str(
                1 / (self.o_wins + self.s_wins + self.tables) * self.s_wins))
            print("Probabilitat de victoria Taules:" + "  " + str(
                1 / (self.o_wins + self.s_wins + self.tables) * self.tables))
            if turn < 9:
                print("\n----------------TORN DEL JUGADOR 2 (MINIMAX)----------------")
                n = self.minimax(turn, points, False)
                points = n.points
                self.board[n.x][n.y] = 'S'
                turn += 1
                self.printMinimaxNodes(n, turn)
                self.printBoard()
                print("Probabilitat de victoria Jugador O:" + "  " + str(
                    1 / (self.o_wins + self.s_wins + self.tables) * self.o_wins))
                print("Probabilitat de victoria Jugador S:" + "  " + str(
                    1 / (self.o_wins + self.s_wins + self.tables) * self.s_wins))
                print("Probabilitat de victoria Taules:" + "  " + str(
                    1 / (self.o_wins + self.s_wins + self.tables) * self.tables))
        val = input("\nPrem 1, per tornar a jugar \n")
        if val == "1":
            self.newGame()
            turn = 0
            points = 0

    def oneMinimax(self):
        turn = 0
        points = 0
        while turn < 9:
            self.o_wins = 0
            self.s_wins = 0
            self.tables = 0
            print("\n----------------TORN DEL JUGADOR 1 (MINIMAX)----------------")
            n = self.minimax(turn, points, True)
            points +=self.new_points(n.x, n.y)
            self.board[n.x][n.y] = 'O'
            self.printMinimaxNodes(n, turn)
            self.printBoard()
            print("Probabilitat de victoria Jugador O:"+"  " + str(1 / (self.o_wins + self.s_wins + self.tables) * self.o_wins))
            print("Probabilitat de victoria Jugador S:"+"  " + str(1 / (self.o_wins + self.s_wins + self.tables) * self.s_wins))
            print("Probabilitat de victoria Taules:" + "  " + str(1 / (self.o_wins + self.s_wins + self.tables) * self.tables))
            print("Punts:", points)
            turn += 1
            if turn < 9:
                print("\n--------------------TORN DEL JUGADOR 2--------------------")
                pos = self.selectMove()
                self.board[pos[0]][pos[1]] = 'S'
                points += self.new_points(pos[0], pos[1])
                turn += 1
                self.minimax(turn, points, True)
                self.printBoard()
                print("Punts:", points)

        if points<0:
            winner = 'S'
        elif points>0:
            winner = 'O'
        else:
            winner = "Taules"
        print('\x1b[6;30;42m' + "Ha guanyar el jugador: "+winner + '\x1b[0m')
        val = input("\nPrem 1, per tornar a jugar \n")
        if val == "1":
            self.newGame()
            turn = 0
            points = 0


    def printMinimaxNodes (self, node, turn):
        n = node
        b = [['-'] * (self.size) for _ in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                b[x][y] = self.board[x][y]

        print('\x1b[6;30;42m' +"MINIMAX SEARCH" + '\x1b[0m')
        print()
        for i in range(9-turn):
            b[n.x][n.y] = n.player
            print(b)
            n = n.nextNode
        print()

    def selectModeGame(self):
        print('\x1b[48;5;23m' + "  ------------------  JOC  DE L'OS  ------------------  " + '\x1b[0m')

        print("\n                      Mode de Joc:")
        print("                minimax vs persona: Prem 1")
        print("                minimax vs persona: Prem 2")
        print("  ----------------------------------------------------")

        while True:
            try:
                inputt = int(input())
            except ValueError:
                print("minimax vs persona: Prem 1, minimax vs persona: Prem 2")
                continue

            if inputt != 1 and inputt != 2:
                print("minimax vs persona: Prem 1, minimax vs persona: Prem 2")
                continue
            else:
                break
        return inputt

    def printBoard(self):
        for x in range(self.size):
            print()
            for y in range(self.size):
                print('\x1b[6;30;42m' +self.board[x][y] +" "+ '\x1b[0m', end="")
        print("\n")

    def selectMove(self):
        pos = [0] * (2)
        while True:
            try:
                inputUser = int(input("Escull posició de la X:"))
            except ValueError:
                print("Ha de ser valor numeric entre 0 i 2")
                continue

            if inputUser > 2 or inputUser < 0:
                print("Ha de ser valor numeric entre 0 i 2")
                continue
            else:
                break
        pos[0] = inputUser
        while True:
            try:
                inputUser = int(input("Escull posició de la y:"))
            except ValueError:
                print("Ha de ser valor numeric entre 0 i 2")
                continue

            if inputUser > 2 or inputUser < 0:
                print("Ha de ser valor numeric entre 0 i 2")
                continue
            else:
                break
        pos[1] = inputUser
        if self.board[pos[0]][pos[1]] != "-":
            print("La Casella ja està ocupada, selecciona un altre posició")
            return self.selectMove()
        return pos

    class Node:
        nextNode = None
        x = 0
        y = 0
        player = ' '
        points = 0

        def __init__(self, x, y, player, points, nextNode):
            self.x = x
            self.y = y
            self.player = player
            self.points = points
            self.nextNode = nextNode

    def newGame(self):
        self.board = [['-'] * (self.size) for _ in range(self.size)]
        self.o_wins = 0
        self.s_wins = 0
        self.tables = 0
        self.play()

    def minimax(self, depth, points, maximizingPlayer):
        if depth == self.size * self.size:
            self.update_victories(points)
            return self.Node(-1, -1, 'c', points, None)
        node = None
        if maximizingPlayer:
            bestValue = -1000
            for x in range(self.size):
                for y in range(self.size):
                    if self.board[x][y] == '-':
                        self.board[x][y] = 'O'
                        p = self.new_points(x, y)

                        n = self.minimax(depth + 1, points + p, False)
                        points -= p
                        self.board[x][y] = '-'
                        if n.points > bestValue:
                            bestValue = n.points
                            node = self.Node(x, y, 'O', bestValue, n)
        else:
            bestValue = +1000
            for x in range(self.size):
                for y in range(self.size):
                    if self.board[x][y] == '-':
                        self.board[x][y] = 'S'
                        p = self.new_points(x, y)
                        n = self.minimax(depth + 1, points + p, True)
                        points -= p
                        self.board[x][y] = '-'
                        if n.points < bestValue:
                            bestValue = n.points
                            node = self.Node(x, y, 'S', bestValue, n)
        return node

    def new_points(self, x, y):
        points = 0
        if self.board[x][y] == 'S':
            if x - 1 >= 0 and self.board[x - 1][y] == 'O':
                points -= 1
            if y - 1 >= 0 and self.board[x][y - 1] == 'O':
                points -= 1
        else:
            if x + 1 < self.size and self.board[x + 1][y] == 'S':
                points += 1
            if y + 1 < self.size and self.board[x][y + 1] == 'S':
                points += 1
        return points

    def update_victories(self, points):
        if points > 0:
            self.o_wins += 1
        elif points < 0:
            self.s_wins += 1
        else:
            self.tables += 1




if __name__ == "__main__":
    JocDelOs.main([])

