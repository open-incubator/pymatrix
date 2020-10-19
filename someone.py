from place import Place
from random import randint

class Someone:
    def __init__(self, identifiant, x, y, mall, workplace):
        self.identifiant = identifiant
        self.age = 0
        self.partner = False
        self.friends = []
        self.nothingSpecials = []
        self.x = x
        self.y = y
        self.house = Place(x, y)
        self.mall = mall
        self.workplace = workplace

    def addOneYear(self):
        self.age =+ 1

    def becomePartner(self, someone):
        self.partner = someone

    def becomeFirend(self, someone):
        self.friends.append(someone)

    def becomeNothingSpecial(self, someone):
        self.nothingSpecials.append(someone)

    def isNotInRelationWith(self, identifiant):
        return identifiant not in self.friends and identifiant not in self.nothingSpecials and self.partner != identifiant

    def goToWork(self):
        self.x = self.workplace.x
        self.y = self.workplace.y
        return [self.workplace.x, self.workplace.y]

    def goToHome(self):
        self.x = self.house.x
        self.y = self.house.y
        return [self.house.x, self.house.y]

    def goToShop(self):
        self.x = self.mall.x
        self.y = self.mall.y
        return [self.mall.x, self.mall.y]
