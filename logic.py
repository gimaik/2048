from random import randint


# construct new game
class Matrix():
    def __init__(self, row, col, digit, fill=0):
        self.mat = []
        self.row = row
        self.col = col
        self.fill = fill
        self.digit = digit
        self.done = False

        for i in range(self.row):
            self.mat.append([self.fill] * self.col)

    def __getitem__(self, index):
        return self.mat[index]

    def add_digit(self):
        x = randint(0, len(self.mat) - 1)
        y = randint(0, len(self.mat) - 1)

        while self.mat[x][y] != self.fill:
            x = randint(0, len(self.mat) - 1)
            y = randint(0, len(self.mat) - 1)
        self.mat[x][y] = self.digit

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
            print("up")
            self.transpose()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.transpose()
        elif move_type == "down":
            print("down")
            self.transpose()
            self.reverse()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.reverse()
            self.transpose()
        elif move_type == "left":
            print("left")
            self.cover_up()
            self.merge()
            self.cover_up()
        elif move_type == "right":
            self.reverse()
            self.cover_up()
            self.merge()
            self.cover_up()
            self.reverse()


#hdskjadsak§