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

    def top_left(self):
        map = self.rover.get_map()
        position = self.rover.get_position()
        self.rover.go_forward()
        if ( position.y == map.limitVertical ):
            self.rover.turn_right()


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

    def top_left(self):
        self.turn_left();



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

    def top_left(self):
        position = self.rover.get_position()
        map = self.rover.get_map()
        self.rover.go_forward()
        if ( position.x == map.limitHorizontal ):
            self.rover.turn_left()


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

    def top_left(self):
        self.turn_right();

class Rover:

    def __init__(self,position,aspect,map = None):
        self.position = position
        self.set_aspect(aspect)
        self.map = map

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

    def top_left(self):
        position = self.get_position()
        map = self.get_map()
        while (position.x < map.limitHorizontal) or (position.y < map.limitVertical):
            self.state.top_left()

    def set_aspect_state(self,aspect):

        aspects = {
            'N': RoverAspectNorth(self),
            'S': RoverAspectSouth(self),
            'E': RoverAspectEast(self),
            'W': RoverAspectWest(self)
        }
        return aspects[aspect]

    def get_map(self):
        return self.map