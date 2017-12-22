from random import choice

class RandomWalk():
    """ A class to generate a RandomWalk data """
    
    def __init__(self, num_points = 5000):
        """ Initiate random walk attributes """
        self.num_points = num_points
        
        # All random walk start from (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # Decide moving direction and distance
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """ Calculate points included by random walk """
        
        # Random walk until meet the designated distance
        while len(self.x_values) < self.num_points:
            
            # Decide moving direction and distance
#            x_direction = choice([1, -1])
#            x_distance = choice([0, 1, 2, 3, 4])
#            x_step = x_direction * x_distance

            x_step = self.get_step()
            y_step = self.get_step()
            
#            y_direction = choice([1, -1])
#            y_distance = choice([0, 1, 2, 3, 4])
#            y_step = y_direction * y_distance
            
            # Don't walk with moving forward
            if x_step ==0 and y_step == 0:
                continue
                
            # Calculate next x & y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
            
            
            
