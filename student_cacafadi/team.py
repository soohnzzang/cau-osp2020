import unittest
from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer
from loa.judge import EachTurnMaxSurvivalJudge
from loa.simulator import BasicSimulator
from loa.logging import use_logging, finish_logging

def get_team():
    return MyTeam("휙휙")

class O(Unit):
    
    HP = 11 # Hit Points (health points)    
    ATT = 14 # Attack
    ARM = 16.3  # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
class I(Unit): #뻐기기
    # X + 1.5Y >= 50
    HP = 18 # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 21.333 # Armor
    EVS = 0 # Evasion
        
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
        self.units.append(I(self, "Unit1-01", 0))
        self.units.append(I(self, "Unit1-01", 1))  
        self.units.append(I(self, "Unit1-01", 2))
        self.units.append(I(self, "Unit1-01", 3))        
        self.units.append(I(self, "Unit1-01", 4))        
        self.units.append(I(self, "Unit1-01", 5))    
        self.units.append(I(self, "Unit1-01", 6))
        self.units.append(I(self, "Unit1-01", 7))        
        self.units.append(I(self, "Unit1-01", 8))   
        self.units.append(I(self, "Unit1-01", 9))
        
    def arrange(self, enemy: Team):
        first_unit = self.units[0]
        for i in range(self.num_positions - 1):
            j = i + 1 
            self.units[i] = self.units[j]
            if self.units[i] != None:
               self.units[i].pos = i 
        # end of for
        self.units[-1] = first_unit
        if self.units[-1] != None:
            self.units[-1].pos = self.num_positions - 1
            
class TestTeam(unittest.TestCase):
    
    def test_team(self):
        team=MyTeam("휙휙")
        examiner=TeamExaminer()
        examiner.check(team)
        examiner.check(team)
   
if __name__ == "__main__":
    unittest.main()
