class Player:

    def __init__(self,first_name,last_name,position,batting_order):
        self.firstName = first_name
        self.lastName = last_name
        self.position = position
        self.battingOrder = batting_order

    def full_name(self):
        fullname = self.firstName + ' ' + self.lastName
        print(fullname)