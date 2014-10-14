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
        self.rover.set_aspect("E")

class RoverAspectSouth:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.y -= 1

    def go_backward(self):
        self.rover.position.y += 1

class RoverAspectEast:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.x += 1

    def go_backward(self):
        self.rover.position.x -= 1

class RoverAspectWest:
    def __init__(self,rover):
        self.rover = rover

    def go_forward(self):
        self.rover.position.x -= 1

    def go_backward(self):
        self.rover.position.x += 1

class Rover:

    def __init__(self,position,aspect):
        self.position = position
        self.aspect = aspect;
        self.state = self.set_aspect_state(aspect)



    def get_position(self):
        return self.position

    def get_aspect(self):
        return self.aspect

    def set_aspect(self, aspect):
        self.aspect = aspect

    def go_forward(self):
        self.state.go_forward()

    def go_backward(self):
        self.state.go_backward()

    def turn_left(self):
        self.state.turn_left()

    def get_aspect(self):

        return self.aspect

    def set_aspect_state(self,aspect):

        if aspect == 'N':
            return RoverAspectNorth(self)
        elif aspect == 'S':
            return RoverAspectSouth(self)
        elif aspect == 'E':
            return RoverAspectEast(self)
        elif aspect == 'W':
            return RoverAspectWest(self)

