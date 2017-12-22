from random import randint

class Die():
    """ A class for die """
    
    def __init__(self, num_sides=6):
        """ Default sides of die is 6 """
        self.num_sides = num_sides
                
    def roll(self):
        """ Return a random number in (1, 6) for a die side """
        return randint(1, self.num_sides)
        
