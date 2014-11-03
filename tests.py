import unittest
from rover import Rover
from remote_control import RemoteControl
from map import Map

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


    def test_command_string(self):

        rover = Rover(P(0,0),'N')
        control = RemoteControl(rover)
        control.execute('f')

        self.assertEqual(rover.get_position().x, 0)
        self.assertEqual(rover.get_position().y, 1)

    def test_command_other_string(self):

        rover = Rover(P(0,0),'E')
        control = RemoteControl(rover)
        control.execute('f')

        self.assertEqual(rover.get_position().x, 1)
        self.assertEqual(rover.get_position().y, 0)

        control.execute('b')

        self.assertEqual(rover.get_position().x, 0)
        self.assertEqual(rover.get_position().y, 0)

        control.execute('ff')

        self.assertEqual(rover.get_position().x, 2)
        self.assertEqual(rover.get_position().y, 0)

        control.execute('lfff')

        self.assertEqual(rover.get_position().x, 2)
        self.assertEqual(rover.get_position().y, 3)

    def test_command_other_path(self):

        rover = Rover(P(0,0),'N')
        control = RemoteControl(rover)
        control.execute('ffrff')

        self.assertEqual(rover.get_position().x, 2)
        self.assertEqual(rover.get_position().y, 2)

    def test_command_top_left_from_E(self):
        map = Map(10,10)
        rover = Rover(P(0,0),'E',map)

        control = RemoteControl(rover)
        control.execute('t')

        self.assertEqual(rover.get_position().x, 10)
        self.assertEqual(rover.get_position().y, 10)

    def test_command_top_left_from_S(self):
        map = Map(10,10)
        rover = Rover(P(0,0),'S',map)

        control = RemoteControl(rover)
        control.execute('t')

        self.assertEqual(rover.get_position().x, 10)
        self.assertEqual(rover.get_position().y, 10)

    def test_map_with_obstaces(self):
        map = Map(10,10)
        map.set_obstacles([
            P(2,2),
            P(5,5),
            P(5,6)
        ])

        self.assertTrue(map.is_free(P(0,0)))
        self.assertFalse(map.is_free(P(2,2)))
    '''
    def test_command_top_left_diferent_grid(self):
        map = Map(10,10)
        map.setObstacles([
            P(2,2),
            P(5,5),
            p(5,6)
        ])

        rover = Rover(P(0,0),'N',map)

        control = RemoteControl(rover)
        control.execute('t')

        self.assertEqual(rover.get_position().x, 10)
        self.assertEqual(rover.get_position().y, 10)
    '''

if __name__ == '__main__':
    unittest.main()

