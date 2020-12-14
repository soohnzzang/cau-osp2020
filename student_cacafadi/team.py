import unittest
from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer
from loa.judge import EachTurnMaxSurvivalJudge
from loa.simulator import BasicSimulator
from loa.logging import use_logging, finish_logging

def get_team():
    return MyTeam("⚡Benzi⚡")

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
       


class MyTeam(Team):
    def initialize(self):
        for i in range(10):
            unit = MyUnit1(self, "A-Unit%02d"%(i+1), i)
            self.units.append(unit)
            
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
