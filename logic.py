from random import randint, choice


# construct new game
class Matrix():
    def __init__(self, row, col, digit, fill=0):
        self.mat = []
        self.row = row
        self.col = col
        self.fill = fill
        self.digit = digit
        self.done = False
        self.score = 0

        for i in range(self.row):
            self.mat.append([self.fill] * self.col)

    def __getitem__(self, index):
        return self.mat[index]

    def check_not_filled(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.mat[i][j] == self.fill:
                    return True
        return False

    def score(self):
        for i in range(self.row):
            for j in range(self.col):
                self.score += self.mat[i][j]

    def add_digit(self):
        x = randint(0, len(self.mat) - 1)
        y = randint(0, len(self.mat) - 1)

        if self.check_not_filled():
            while self.mat[x][y] != self.fill:
                x = randint(0, len(self.mat) - 1)
                y = randint(0, len(self.mat) - 1)
            self.mat[x][y] = self.digit**choice([1,2])

    def game_state(self):
        for i in range(self.col):
            for j in range(self.row):
                if self.mat[i][j]==2048:
                    return "Win"

        for i in range(self.col-1):
            for j in range(self.row-1):
                if self.mat[i][j]==self.mat[i+1][j] or self.mat[i][j+1]==self.mat[i][j]:
                    return "Not Over"

        for i in range(self.col):
            for j in range(self.row):
                if self.mat[i][j]==self.fill:
                    return "Not Over"

        for k in range(self.col-1):
            if self.mat[self.row-1][k]==self.mat[self.row-1][k+1]:
                return "Not Over"

        for j in range(self.row-1):
            if self.mat[j][self.col-1]==self.mat[j+1][self.col-1]:
                return "Not Over"
        return "Lose"

    def reverse(self):
        for i in range(self.row):
            self.mat[i] = self.mat[i][::-1]

    def transpose(self):
        self.mat = list(map(list, zip(*self.mat)))
        self.row, self.col = self.col, self.row

    def merge(self):
        self.done = False
        for i in range(self.row):
            for j in range(self.col - 1):
                if self.mat[i][j] == self.mat[i][j + 1] and self.mat[i][j] != self.fill:
                    self.mat[i][j] *= self.digit
                    self.mat[i][j + 1] = self.fill
                    self.done = True

    def cover_up(self):
        mat_ = []
        self.done = False
        for i in range(self.row):
            mat_.append([self.fill] * self.col)

        for i in range(self.row):
            count = 0
            for j in range(self.col):
                if self.mat[i][j] != 0:
                    mat_[i][count] = self.mat[i][j]
                    if j != count:
                        self.done = True
                    count += 1
        self.mat = mat_

    def move(self, move_type):
        if move_type == "up":
            self.transpose()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.transpose()
            self.done = True
        elif move_type == "down":
            self.transpose()
            self.reverse()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.reverse()
            self.transpose()
            self.done = True
        elif move_type == "left":
            self.cover_up()
            self.merge()
            self.cover_up()
            self.done = True
        elif move_type == "right":
            self.reverse()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.reverse()
            self.done = True
