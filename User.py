class User:
    
    currentIndex: str
    userID: str 
    funvalue: int
    attack: int
    magic: int
    armour: int
    skill: int
    Ny_Know: int
    Pm_Know: int
    El_Know: int
    Br_KNow: int

    def __init__(self, userID):
        
        self.userID = userID
        self.funvalue = 0
        self.attack = 1
        self.magic = 1
        self.armour = 1
        self.skill = 1
        self.Ny_Know = 0
        self.Pm_Know = 0
        self.El_Know = 0
        self.Br_Know = 0

