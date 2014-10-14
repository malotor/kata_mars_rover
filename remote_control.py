class RemoteControl:
    def __init__(self,rover):
        self.rover = rover

    def execute(self,commands):
        for command in commands:
            if command == 'f':
                self.rover.go_forward()
            elif command == 'b':
                self.rover.go_backward()
            elif command == 'l':
                self.rover.turn_left()
            elif command == 'r':
                self.rover.turn_right()