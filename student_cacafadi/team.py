import unittest
from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer
from loa.judge import EachTurnMaxSurvivalJudge
from loa.simulator import BasicSimulator
from loa.logging import use_logging, finish_logging

def get_team():
    return MyTeam("😶DDRS")

class benzi(Unit):
    
    HP = 32 # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 11  # Armor
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
            unit = benzi(self, "unit%02d"%(i+1), i)
            self.units.append(unit)
       
    
    def arrange(self, enemy: Team):
        for i in range(self.num_positions):
            if self.units[i]!=None:
                for j in range(enemy.num_positions):
                    if enemy.units[j]==None:
                        if self.units[j]==None:
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=None
                            break
        for i in range(self.num_positions):
            if self.units[i]!=None:
                for j in range(enemy.num_positions):
                    if enemy.units[j]!=None and enemy.units[j].att>self.units[i].arm+1:
                        if self.units[j]==None:
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=None
                            break
                        elif self.units[j]!=None and enemy.units[j].att>self.units[j].arm+1:
                            pass
                        else:
                            temp=self.units[j]
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=temp
                            self.units[i].pos=i
                            break
        for i in range(self.num_positions):
            if self.units[i]!=None:
                for j in range(enemy.num_positions):
                    if enemy.units[j]!=None and enemy.units[j].hp<=self.units[i].hp:
                        if self.units[j]==None:
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=None
                            break
                        elif self.units[j]!=None and self.units[j].hp>=self.units[i].hp:
                            pass
                        else:
                            temp=self.units[j]
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=temp
                            self.units[i].pos=i
                            break
class TestTeam(unittest.TestCase):
    
    def test_team(self):
        team=MyTeam("DRDDS")
        examiner=TeamExaminer()
        examiner.check(team)
        examiner.check(team)
   
if __name__ == "__main__":
    unittest.main()
