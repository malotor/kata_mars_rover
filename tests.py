import unittest
from rover import Rover

from rover import Position as P

#from mock import Mock

# The following is the class in which all functions will be ran by unittest
class RoverTest(unittest.TestCase):

    def setUp(self):
        self.rover = Rover(P(0,0),'N')

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
        self.assertEqual(rover.get_position().x, 51)
        rover.go_forward()
        self.assertEqual(rover.get_position().x, 52)

    def test_rover_go_forward_S(self):
        rover = Rover(P(50,50),'S')
        rover.go_forward()
        self.assertEqual(rover.get_position().x, 49)
        rover.go_forward()
        self.assertEqual(rover.get_position().x, 48)
    def test_rover_go_forward_E(self):
        rover = Rover(P(50,50),'E')
        rover.go_forward()
        self.assertEqual(rover.get_position().y, 51)
        rover.go_forward()
        self.assertEqual(rover.get_position().y, 52)
    def test_rover_go_forward_W(self):
        rover = Rover(P(50,50),'W')
        rover.go_forward()
        self.assertEqual(rover.get_position().y, 49)
        rover.go_forward()
        self.assertEqual(rover.get_position().y, 48)


if __name__ == '__main__':
    unittest.main()

