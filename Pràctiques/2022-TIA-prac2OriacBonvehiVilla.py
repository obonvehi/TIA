import random


class JocCavall:   # Warnsdorff's heuristic

    N = 8
    cx = [1, 1, 2, 2, -1, -1, -2, -2]
    cy = [2, -2, 1, -1, 2, -2, 1, -1]

    def limits(self, x, y):
        return 0 <= x < JocCavall.N and 0 <= y < JocCavall.N

    def isempty(self, a, x, y):
        return (self.limits(x, y)) and (a[y * JocCavall.N + x] < 0)

    def get_degree(self, a, x, y):
        count = 0
        for i in range(JocCavall.N):
            if self.isempty(a, (x + JocCavall.cx[i]), (y + JocCavall.cy[i])):
                count += 1
            i += 1
        return count

    def next_move(self, a, casella):
        min_deg_idx = -1
        c = 0
        min_deg = (JocCavall.N + 1)
        nx = 0
        ny = 0
        start = random.randint(0, self.N - 1)
        for count in range(JocCavall.N):
            i = (start + count) % JocCavall.N
            nx = casella.x + JocCavall.cx[i]
            ny = casella.y + JocCavall.cy[i]
            c = self.get_degree(a, nx, ny)
            if (self.isempty(a, nx, ny)) and (c < min_deg):
                min_deg_idx = i
                min_deg = c
            count += 1
        if min_deg_idx == -1:
            return None
        nx = casella.x + JocCavall.cx[min_deg_idx]
        ny = casella.y + JocCavall.cy[min_deg_idx]
        a[ny * JocCavall.N + nx] = a[casella.y * JocCavall.N + casella.x] + 1
        casella.x = nx
        casella.y = ny
        return casella

    def print(self, a):
        for i in range(JocCavall.N):
            for j in range(JocCavall.N):
                print("%d\t" % (a[j * JocCavall.N + i]), end="", sep="")
                j += 1
            print("\n")
            i += 1

    def neighbour(self, x, y, xx, yy):
        for i in range(JocCavall.N):
            if (x + JocCavall.cx[i]) == xx and (y + JocCavall.cy[i]) == yy:
                return True
            i += 1
        return False

    def find_closed(self, sx, sy):
        a = [0] * (JocCavall.N * JocCavall.N)
        for i in range(JocCavall.N * JocCavall.N):
            a[i] = -1

        casella = Casella(sx, sy)
        a[casella.y * JocCavall.N + casella.x] = 1
        ret = None
        for i in range(JocCavall.N * JocCavall.N - 1):
            ret = self.next_move(a, casella)
            if ret is None:
                return False
            i += 1
        if not self.neighbour(ret.x, ret.y, sx, sy):
            return False
        self.print(a)
        return True

    @staticmethod
    def main(args):
        is_good = False
        x = 0
        y = 0
        while not is_good:
            try:
                x = int(input("Introdueix punt de partida del eix X (1 al 7): "))
                y = int(input("Introdueix punt de partida del eix Y (1 al 7): "))
                if 0 < x < 8 and 0 < y < 8:
                    is_good = True
                else:
                    print("Els numeros introduits estan fora del rang (1-7)")
            except:
                print("Els valors han de ser numerics")

        is_good = False
        while not is_good:
            is_good = JocCavall().find_closed(x, y)


class Casella:
    x = 1
    y = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    JocCavall.main([])
