
class PropertyClass():
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
    #@property
    def getHeight(self):
        return self.__height
    #@setHeight.setter
    def setHeight(self, height):
        self.__height = height
    #@property
    def getWidth(self):
        return self.__width
    #@setWidth.setter
    def setWidth(self, width):
        self.__width = width
    