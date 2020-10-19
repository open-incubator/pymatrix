class Place:
    def __init__(self, x, y):
        self.people = []
        self.x = x
        self.y = y

    def addSomeone(self, someone):
        self.people.append(someone)

    def showCoords(self):
        print('X: ',self.x,' / Y: ', self.y)
