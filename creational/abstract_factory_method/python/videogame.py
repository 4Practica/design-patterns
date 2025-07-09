from abc import ABC, abstractmethod


class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def special_ability(self):
        pass
    
class EnemyFactory(ABC):
    @abstractmethod
    def create_wheel_chair_enemy(self)->Enemy:
        pass
    @abstractmethod
    def create_flier_enemy(self)->Enemy:
        pass
    @abstractmethod
    def create_boss_enemy(self)->Enemy:
        pass


class BossGhost(Enemy):
    def __init__(self, health=120, speed=2.0, ai_level=6):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "devastador fantasmal "
    def move(self):
        return "silla"
    def special_ability(self):
        return "silla"

class FlierGhost(Enemy):
    def __init__(self, health=50, speed=3.0, ai_level=4):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "aire fantasmal "
    def move(self):
        return "aire"
    def special_ability(self):
        return "aire"


    
class WheelChairGhost(Enemy):
    def __init__(self, health=60, speed=1.5, ai_level=3):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "silla fantasmal "
    def move(self):
        return "silla"
    def special_ability(self):
        return "silla"
    
class GhostFactory(EnemyFactory):
    def create_wheel_chair_enemy(self)->WheelChairGhost:
        return WheelChairGhost()
    def create_flier_enemy(self)->FlierGhost:
        return FlierGhost()
    def create_boss_enemy(self)->BossGhost:
        return BossGhost()

    

class WheelChairZombie(Enemy):
    def __init__(self, health=120, speed=0.5, ai_level=1):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "silla mordiscos "
    def move(self):
        return "silla"
    def special_ability(self):
        return "silla"
    
class BossZombie(Enemy):
    def __init__(self, health=200, speed=1.2, ai_level=5):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "autoridad mordiscos "
    def move(self):
        return "autoridad"
    def special_ability(self):
        return "autoridad"
    def get_stats(self):
        return({ 
            "name": "BossZombie",
            "health": self.health,
            "speed": self.speed,
            "ai_level": self.ai_level})

class FlierZombie(Enemy):
    def __init__(self, health=80, speed=1.8, ai_level=2):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "vuela mordiscos "
    def move(self):
        return "vuela"
    def special_ability(self):
        return "vuela"

class ZombieFactory(EnemyFactory):
    def create_wheel_chair_enemy(self)->WheelChairZombie:
        return WheelChairZombie()      
    def create_flier_enemy(self)->FlierZombie:
        return FlierZombie()       
    def create_boss_enemy(self)->BossZombie:
        return BossZombie()     

class WheelChairRobot(Enemy):
    def __init__(self, health=180, speed=1.0, ai_level=4):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "silla láseres "
    def move(self):
        return "silla"
    def special_ability(self):
        return "silla"
    
class BossRobot(Enemy):
    def __init__(self, health=300, speed=1.8, ai_level=7):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "convocar láseres "
    def move(self):
        return "convocar"
    def special_ability(self):
        return "convocar"
    
    
class FlierRobot(Enemy):
    def __init__(self, health=150, speed=2.5, ai_level=5):
        self.health = health
        self.speed = speed
        self.ai_level = ai_level
        self.name = self.__class__.__name__
    def attack(self):
        return "vuela láseres "
    def move(self):
        return "vuela"
    def special_ability(self):
        return "vuela"
    


class RobotFactory(EnemyFactory):
    def create_wheel_chair_enemy(self)->WheelChairRobot:
        return WheelChairRobot()       
    def create_flier_enemy(self)->FlierRobot:
        return FlierRobot()      
    def create_boss_enemy(self)->BossRobot:
        return BossRobot()      
