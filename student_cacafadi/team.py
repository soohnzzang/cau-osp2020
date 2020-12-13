import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return MyTeam("⚡Benzi⚡")

class Fivedollar(Unit):
    
    HP = 10  # Hit Points (health points)    
    ATT = 19.7 # Attack
    ARM = 10  # Armor
    EVS = 1 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
class Tendollar(Unit):
    
    HP = 0.1  # Hit Points (health points)    
    ATT = 0.1  # Attack
    ARM = 0.1  # Armor
    EVS = 0.1 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)




class MyTeam(Team):
    def initialize(self):
        self.units.append(Fivedollar(self, "Unit1-01", 0))
        self.units.append(Tendollar(self, "Unit1-01", 1))  
        self.units.append(Fivedollar(self, "Unit1-01", 2))
        self.units.append(Tendollar(self, "Unit1-01", 3))        
        self.units.append(Fivedollar(self, "Unit1-01", 4))        
        self.units.append(Tendollar(self, "Unit1-01", 5))    
        self.units.append(Fivedollar(self, "Unit1-01", 6))
        self.units.append(Tendollar(self, "Unit1-01", 7))        
        self.units.append(Fivedollar(self, "Unit1-01", 8))   
        self.units.append(Tendollar(self, "Unit1-01", 9))
        
    def arrange(self, enemy: Team):        
        pass
    
            
class TestTeam(unittest.TestCase):
    
    def test_team(self):
        team=MyTeam("⚡Benzi⚡")
        examiner=TeamExaminer()
        examiner.check(team)
        examiner.check(team)
   
if __name__ == "__main__":
    unittest.main()
