class Player:
    def __init__(self,first_Name,last_Name,position,batting_order):
        self.firstName = first_Name
        self.lastName = last_Name
        self.position = position
        self.battingOrder = batting_order

    def full_name(self):
        fullname = self.firstName + ' ' + self.lastName
        print(fullname)