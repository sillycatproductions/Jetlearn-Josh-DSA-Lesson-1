class Sweets:
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
    
    def show_sweets(self):
        print('I am a {} and i am {}. I am shaped like a/an {} and I taste {}!'. format(self.name, self.color, self.shape, self.taste))

    
#object for Fruit class
sweet1 = Sweets('any color in the rainbow', 'bear', 'sweet', 'Haribo')
sweet1.show_sweets()

sweet2 = Sweets('yellow and green', 'circle', 'sour', 'Sour Waste')
sweet2.show_sweets()
sweet2.set_shape('oval')
sweet2.show_sweets()