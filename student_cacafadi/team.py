
import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return Team("Benzi")

class MyUnit1(Unit):
    
    HP = 7  # Hit Points (health points)    
    ATT = 10  # Attack
    ARM = 4  # Armor
    EVS = 9 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class MyUnit2(Unit):
    
    HP = 7  # Hit Points (health points)    
    ATT = 9  # Attack
    ARM = 5  # Armor
    EVS = 9 # Evasion
        
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
        for i in range(10):
            unit = MyUnit1(self, "A-Unit%02d"%(i+1), i)
            self.units.append(unit)
            
    def arrange(self, enemy: Team):        
        pass
    
            
class TestTeam(unittest.TestCase):
    
    def test_team(self):
        team=MyTeam("Benzi")
        examiner=TeamExaminer()
        examiner.check(team)
        examiner.check(team)
   
if __name__ == "__main__":
    unittest.main()