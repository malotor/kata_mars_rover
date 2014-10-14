class Command:
    def __init__(self,rover):
        self.rover = rover

class CommandForward(Command):
    def execute(self):
        self.rover.go_forward()

class CommandBackward(Command):
    def execute(self):
        self.rover.go_backward()

class CommandLeft(Command):
    def execute(self):
        self.rover.turn_left()

class CommandRight(Command):
    def execute(self):
        self.rover.turn_right()

class RemoteControl:
    def __init__(self,rover):
        self.rover = rover
        self.commands = {
            'f': CommandForward(self.rover),
            'b': CommandBackward(self.rover),
            'l': CommandLeft(self.rover),
            'r': CommandRight(self.rover)
        }

    def execute(self,commandString):
        for command in commandString:
            self.commands[command].execute()