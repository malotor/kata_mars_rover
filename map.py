class Map:

    def __init__(self, limitHorizontal, limitVertical ):
        self.limitVertical = limitVertical
        self.limitHorizontal = limitHorizontal

    def set_obstacles(self,obstacles):
        self.obstacles = obstacles

    def is_free(self,position):
        result = True
        for obstacle in self.obstacles:
            if position == obstacle:
                result = False
        return result