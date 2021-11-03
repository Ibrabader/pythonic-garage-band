

from abc import abstractclassmethod


class Musician:
    members = []

    def __init__(self, name):

        self.name = name
        # Musician.members.append(self)

    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __repr__(self):
        pass

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def __str__(self):
        return "My name is {} and I play guitar".format(self.name)
    def __repr__(self):
        return "Guitarist instance. Name = {}" .format(self.name)
    def get_instrument(self):
        return "guitar"

    def play_solo(self):

        return "face melting guitar solo"

class Drummer(Musician):
    def __str__(self):
        return "My name is {} and I play drums".format(self.name)
    def __repr__(self):
        return "Drummer instance. Name = {}".format(self.name)
    def get_instrument(self):
        return "drums"

    def play_solo(self):

        return "rattle boom crash"



class Bassist(Musician):
    def __str__(self):

        return f"My name is {self.name} and I play bass"

    def __repr__(self):

        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):

        return "bom bom buh bom"


class Band:
    instances=[]
    def __init__(self, name:str, members=[]):
        self.name = name

        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        arrSolos = []
        for member in self.members:
            arrSolos.append(member.play_solo())
        return arrSolos
    
    @classmethod
    def to_list(cls):
        return cls.instances

    if __name__ == "__main__":
        ibrahim= Bassist('Ibrahim')
        print(ibrahim.name)
        print(ibrahim.get_instrument())
        print(ibrahim.play_solo())