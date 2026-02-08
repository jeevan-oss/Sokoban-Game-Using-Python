import os
import copy

class Level:

    def __init__(self, set_name, level_num):

        # Use instance variables 
        self.matrix = []
        self.matrix_history = []

        # Load level file
        level_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'levels',
            set_name,
            f'level{level_num}'
        )

        with open(level_path, 'r') as f:
            for row in f.read().splitlines():
                self.matrix.append(list(row))

    def __del__(self):
        pass

    def getMatrix(self):
        return self.matrix

    def addToHistory(self, matrix):
        self.matrix_history.append(copy.deepcopy(matrix))

    def getLastMatrix(self):
        if len(self.matrix_history) > 0:
            lastMatrix = self.matrix_history.pop()
            self.matrix = lastMatrix
            return lastMatrix
        else:
            return self.matrix

    def getPlayerPosition(self):
        # Iterate rows
        for y, row in enumerate(self.matrix):
            # Iterate columns
            for x, cell in enumerate(row):
                if cell == "@":
                    return [x, y]
        return None

    def getBoxes(self):
        boxes = []
        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                if cell == "$":
                    boxes.append([x, y])
        return boxes

    def getSize(self):
        max_row_length = max(len(row) for row in self.matrix)
        return [max_row_length, len(self.matrix)]
