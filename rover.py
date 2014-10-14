class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class RoverAspectNorth:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.y += 1

    def go_backward(self):
        self.rover.position.y -= 1

    def turn_left(self):
        self.rover.set_aspect("W")

    def turn_right(self):
        self.rover.set_aspect("E")

class RoverAspectSouth:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.y -= 1

    def go_backward(self):
        self.rover.position.y += 1

    def turn_left(self):
        self.rover.set_aspect("E")

    def turn_right(self):
        self.rover.set_aspect("W")


class RoverAspectEast:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.x += 1

    def go_backward(self):
        self.rover.position.x -= 1

    def turn_left(self):
        self.rover.set_aspect("N")

    def turn_right(self):
        self.rover.set_aspect("S")

class RoverAspectWest:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.x -= 1

    def go_backward(self):
        self.rover.position.x += 1

    def turn_left(self):
        self.rover.set_aspect("S")

    def turn_right(self):
        self.rover.set_aspect("N")

class Rover:

    def __init__(self,position,aspect):
        self.position = position
        self.set_aspect(aspect);

    def get_position(self):
        return self.position

    def get_aspect(self):
        return self.aspect

    def set_aspect(self, aspect):
        self.state = self.set_aspect_state(aspect)
        self.aspect = aspect

    def go_forward(self):
        self.state.go_forward()

    def go_backward(self):
        self.state.go_backward()

    def turn_left(self):
        self.state.turn_left()

    def turn_right(self):
        self.state.turn_right()

    def set_aspect_state(self,aspect):

        aspects = {
            'N': RoverAspectNorth(self),
            'S': RoverAspectSouth(self),
            'E': RoverAspectEast(self),
            'W': RoverAspectWest(self)
        }
        return aspects[aspect]


