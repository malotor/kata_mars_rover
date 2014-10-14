import unittest
from rover import Rover

from rover import Position as P

#from mock import Mock

# The following is the class in which all functions will be ran by unittest
class RoverTest(unittest.TestCase):

    # Functions beginning with "test" will be ran as a unit test.
    def test_create_rover(self):
        rover = Rover(P(10,2),'N')
        self.assertEqual(rover.get_position().x, 10)
        self.assertEqual(rover.get_position().y, 2)
        self.assertEqual(rover.get_aspect(), 'N')

        second_rover = Rover(P(15,29),'S')
        self.assertEqual(second_rover.get_position().x, 15)
        self.assertEqual(second_rover.get_position().y, 29)
        self.assertEqual(second_rover.get_aspect(), 'S')

    def test_rover_go_forward(self):
        rover = Rover(P(50,50),'N')
        rover.go_forward()
        self.assertEqual(rover.get_position().y, 51)
        rover.go_forward()
        self.assertEqual(rover.get_position().y, 52)

    def test_rover_go_forward_S(self):
        rover = Rover(P(50,50),'S')
        rover.go_forward()
        self.assertEqual(rover.get_position().y, 49)

    def test_rover_go_forward_E(self):
        rover = Rover(P(50,50),'E')
        rover.go_forward()
        self.assertEqual(rover.get_position().x, 51)

    def test_rover_go_forward_W(self):
        rover = Rover(P(50,50),'W')
        rover.go_forward()
        self.assertEqual(rover.get_position().x, 49)

    def test_rover_go_backward(self):
        rover = Rover(P(50,50),'N')
        rover.go_backward()
        self.assertEqual(rover.get_position().y, 49)

    def test_rover_go_backward_S(self):
        rover = Rover(P(50,50),'S')
        rover.go_backward()
        self.assertEqual(rover.get_position().y, 51)

    def test_rover_go_backward_E(self):
        rover = Rover(P(50,50),'E')
        rover.go_backward()
        self.assertEqual(rover.get_position().x, 49)

    def test_rover_go_backward_W(self):
        rover = Rover(P(50,50),'W')
        rover.go_backward()
        self.assertEqual(rover.get_position().x, 51)


    def test_from_turn_left(self):
        rover = Rover(P(50,50),'N')
        rover.turn_left()
        self.assertEqual(rover.get_position().x, 50)
        self.assertEqual(rover.get_position().y, 50)
        self.assertEqual(rover.get_aspect(), 'W')

        rover.turn_left()
        self.assertEqual(rover.get_aspect(), 'S')

        rover.turn_left()
        self.assertEqual(rover.get_aspect(), 'E')

        rover.turn_left()
        self.assertEqual(rover.get_aspect(), 'N')

    def test_from_turn_right(self):
        rover = Rover(P(50,50),'N')
        rover.turn_right()
        self.assertEqual(rover.get_position().x, 50)
        self.assertEqual(rover.get_position().y, 50)
        self.assertEqual(rover.get_aspect(), 'E')

        rover.turn_right()
        self.assertEqual(rover.get_aspect(), 'S')

        rover.turn_right()
        self.assertEqual(rover.get_aspect(), 'W')

        rover.turn_right()
        self.assertEqual(rover.get_aspect(), 'N')

    def test_from_movement(self):
        rover = Rover(P(50,50),'N')

        rover.turn_right()

        rover.go_forward() # (51,50)
        rover.go_forward() # (52,50)

        rover.turn_left()

        rover.go_backward() # (52,49)
        rover.go_backward() # (52,48)

        self.assertEqual(rover.get_position().x, 52)
        self.assertEqual(rover.get_position().y, 48)


if __name__ == '__main__':
    unittest.main()

