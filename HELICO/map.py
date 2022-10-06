from utils import randbool
from utils import randcell
from utils import randcell2

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп
# 5 - огонь

# TYPE_BORDER = "⬛"
TYPE_BORDER = "░"
# CELL_TYPES = " 🌳🌊🏥🏪🔥🚁"
CELL_TYPES = " ‡□☺☻█◙○●"

TYPE_FIELD = 0
TYPE_FOREST = 1
TYPE_RIVER = 2
TYPE_HOSPITAL = 3
TYPE_SHOP = 4
TYPE_FIRE = 5
TYPE_HELICO = 6
TYPE_CLOUD0 = 7
TYPE_CLOUD1 = 8
TREE_BONUS = 100
UPGRADE_COST = 500
LIVE_COST = 500


class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(5, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_shop()
        self.generate_hospital()

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def print_map(self, helico, clouds):
        # print("#" * (self.w + 2))
        print(TYPE_BORDER * (self.w + 2))
        for ri in range(self.h):
            # print('#', end='')
            print(TYPE_BORDER, end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if clouds.cells[ri][ci] == TYPE_CLOUD0:
                    print(CELL_TYPES[TYPE_CLOUD0], end='')
                elif clouds.cells[ri][ci] == TYPE_CLOUD1:
                    print(CELL_TYPES[TYPE_CLOUD1], end='')
                elif helico.x == ri and helico.y == ci:
                    print(CELL_TYPES[TYPE_HELICO], end='')
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
            # print('#', end='')
            print(TYPE_BORDER, end='')
            print()
        # print("#" * (self.w + 2))
        print(TYPE_BORDER * (self.w + 2))

    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = TYPE_RIVER
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = TYPE_RIVER
                rx, ry = rx2, ry2
                l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = TYPE_FOREST

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        # if self.check_bounds(cx, cy) and self.cells[cx][cy] == 0:
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = TYPE_FOREST

    def generate_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = TYPE_SHOP

    def generate_hospital(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != TYPE_SHOP:
            self.cells[cx][cy] = TYPE_HOSPITAL
        else:
            self.generate_hospital()

    def add_fire(self):
        f = randcell(self.w, self.h)
        fx, fy = f[0], f[1]
        if self.cells[fx][fy] == TYPE_FOREST:
            self.cells[fx][fy] = TYPE_FIRE

    def update_fire(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == TYPE_FIRE:
                    self.cells[ri][ci] = TYPE_FIELD
        for i in range(5):
            self.add_fire()

    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if c == TYPE_RIVER:
            helico.tank = helico.mxtank
        if c == TYPE_FIRE and helico.tank > 0:
            helico.tank -= 1
            self.cells[helico.x][helico.y] = TYPE_FOREST
            helico.score += TREE_BONUS
        if c == TYPE_SHOP and helico.score >= UPGRADE_COST:
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if c == TYPE_HOSPITAL and helico.score >= LIVE_COST:
            helico.lives += 10
            helico.score -= LIVE_COST
        if d == TYPE_CLOUD1:
            helico.lives -= 1
            if helico.lives == 0:
                helico.game_over()

    def export_data(self):
        return {'cells': self.cells}

    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]
