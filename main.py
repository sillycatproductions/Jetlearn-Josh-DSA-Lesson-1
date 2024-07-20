class Fruit:
    #properties
    def __init__(self, color, shape, taste, name):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.name = name
    #functions
    #getts
    def get_shape(self):
        return self.shape
    #setters
    def set_shape(self, new_shape):
        self.shape = new_shape
    
    def show_fruits(self):
        print('hi i am {} and i am {}, {}, {}'. format(self.name, self.color, self.shape, self.taste))

    
#object for Fruit class
fruit1 = Fruit('red', 'circle', 'sweet', 'apple')
fruit1.show_fruits()

fruit2 = Fruit('yellow', 'stick', 'best fruit', 'banana')
fruit2.show_fruits()



