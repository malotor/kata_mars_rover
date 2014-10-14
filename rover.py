class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rover:

    def __init__(self,position,aspect):
        self.position = position
        self.aspect = aspect

    def get_position(self):
        return self.position

    def get_aspect(self):
        return self.aspect

    def go_forward(self):

        if self.aspect == 'N':
            self.position.x += 1
        elif self.aspect == 'S':
            self.position.x -= 1
        elif self.aspect == 'E':
            self.position.y += 1
        elif self.aspect == 'W':
            self.position.y -= 1
