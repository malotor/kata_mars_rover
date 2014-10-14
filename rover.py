class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class RoverAspectNorth:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.x += 1


class RoverAspectSouth:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.x -= 1

class RoverAspectEast:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.y += 1

class RoverAspectWest:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.y -= 1

class Rover:

    def __init__(self,position,aspect):
        self.position = position
        self.aspect = aspect

        if self.aspect == 'N':
            self.state = RoverAspectNorth(self)
        elif self.aspect == 'S':
            self.state = RoverAspectSouth(self)
        elif self.aspect == 'E':
            self.state = RoverAspectEast(self)
        elif self.aspect == 'W':
            self.state = RoverAspectWest(self)

    def get_position(self):
        return self.position

    def get_aspect(self):
        return self.aspect

    def go_forward(self):
        self.state.go_forward()
