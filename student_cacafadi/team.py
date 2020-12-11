<<<<<<< HEAD
=======
<<<<<<< HEAD

>>>>>>> refs/remotes/origin/main
import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return MyTeam("Benzi")

class dollar(Unit):
    
    HP = 7  # Hit Points (health points)    
    ATT = 9  # Attack
    ARM = 4  # Armor
    EVS = 8 # Evasion
        
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
        self.units.append(dollar(self, "Unit1-01", 0))
        self.units.append(dollar(self, "Unit1-01", 1))  
        self.units.append(dollar(self, "Unit1-01", 2))
        self.units.append(dollar(self, "Unit1-01", 3))        
        self.units.append(dollar(self, "Unit1-01", 4))        
        self.units.append(dollar(self, "Unit1-01", 5))    
        self.units.append(dollar(self, "Unit1-01", 6))
        self.units.append(dollar(self, "Unit1-01", 7))        
        self.units.append(dollar(self, "Unit1-01", 8))   
        self.units.append(dollar(self, "Unit1-01", 9))
        
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
    
<<<<<<< HEAD
=======
    
=======

import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return Team("Benzi")

class dollar(Unit):
    
    HP = 7  # Hit Points (health points)    
    ATT = 9  # Attack
    ARM = 4  # Armor
    EVS = 8 # Evasion
        
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
        self.units.append(dollar(self, "Unit1-01", 0))
        self.units.append(dollar(self, "Unit1-01", 1))  
        self.units.append(dollar(self, "Unit1-01", 2))
        self.units.append(dollar(self, "Unit1-01", 3))        
        self.units.append(dollar(self, "Unit1-01", 4))        
        self.units.append(dollar(self, "Unit1-01", 5))    
        self.units.append(dollar(self, "Unit1-01", 6))
        self.units.append(dollar(self, "Unit1-01", 7))        
        self.units.append(dollar(self, "Unit1-01", 8))   
        self.units.append(dollar(self, "Unit1-01", 9))
        
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
    
    
>>>>>>> fa6853ef576222a4c8a7f045e6da76dc55815590
    
>>>>>>> refs/remotes/origin/main
