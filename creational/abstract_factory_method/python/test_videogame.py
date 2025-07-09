import pytest
from .videogame import (Enemy, EnemyFactory, WheelChairGhost,
    WheelChairZombie, WheelChairRobot,BossGhost,BossZombie,
    BossRobot, FlierGhost,FlierZombie, FlierRobot, 
    GhostFactory, ZombieFactory, RobotFactory)

# ============================================================================
# TESTS CON PYTEST
# ============================================================================

class TestEnemyBase:
    """Tests para la clase base Enemy"""
    
    def test_enemy_abstract_class(self):
        """Test que verifica que Enemy es una clase abstracta"""
        with pytest.raises(TypeError):
            Enemy(health=100, speed=1.0, ai_level=3)
    
    def test_enemy_attributes(self):
        """Test que verifica que los enemigos tienen los atributos correctos"""
        ghost = WheelChairGhost()
        
        assert ghost.health == 60
        assert ghost.speed == 1.5
        assert ghost.ai_level == 3
        assert ghost.name == "WheelChairGhost"
    
    def test_get_stats_method(self):
        """Test que verifica el método get_stats"""
        zombie = BossZombie()
        stats = zombie.get_stats()
        
        expected_stats = {
            "name": "BossZombie",
            "health": 200,
            "speed": 1.2,
            "ai_level": 5
        }
        
        assert stats == expected_stats


class TestWheelChairEnemies:
    """Tests para enemigos en silla de ruedas"""
    
    def test_wheel_chair_ghost_attributes(self):
        """Test que verifica los atributos del fantasma en silla de ruedas"""
        ghost = WheelChairGhost()
        
        assert ghost.health == 60
        assert ghost.speed == 1.5
        assert ghost.ai_level == 3
        assert isinstance(ghost, Enemy)
    
    def test_wheel_chair_zombie_attributes(self):
        """Test que verifica los atributos del zombi en silla de ruedas"""
        zombie = WheelChairZombie()
        
        assert zombie.health == 120
        assert zombie.speed == 0.5
        assert zombie.ai_level == 1
        assert isinstance(zombie, Enemy)
    
    def test_wheel_chair_robot_attributes(self):
        """Test que verifica los atributos del robot en silla de ruedas"""
        robot = WheelChairRobot()
        
        assert robot.health == 180
        assert robot.speed == 1.0
        assert robot.ai_level == 4
        assert isinstance(robot, Enemy)
    
    def test_wheel_chair_enemy_behavior(self):
        """Test que verifica el comportamiento de enemigos en silla de ruedas"""
        ghost = WheelChairGhost()
        zombie = WheelChairZombie()
        robot = WheelChairRobot()
        
        # Verificar que los métodos retornan strings
        assert isinstance(ghost.attack(), str)
        assert isinstance(zombie.move(), str)
        assert isinstance(robot.special_ability(), str)
        
        # Verificar que contienen información específica
        assert "silla" in ghost.attack()
        assert "silla" in zombie.move()
        assert "silla" in robot.special_ability()


class TestFlierEnemies:
    """Tests para enemigos voladores"""
    
    def test_flier_ghost_attributes(self):
        """Test que verifica los atributos del fantasma volador"""
        ghost = FlierGhost()
        
        assert ghost.health == 50
        assert ghost.speed == 3.0
        assert ghost.ai_level == 4
        assert isinstance(ghost, Enemy)
    
    def test_flier_zombie_attributes(self):
        """Test que verifica los atributos del zombi volador"""
        zombie = FlierZombie()
        
        assert zombie.health == 80
        assert zombie.speed == 1.8
        assert zombie.ai_level == 2
        assert isinstance(zombie, Enemy)
    
    def test_flier_robot_attributes(self):
        """Test que verifica los atributos del robot volador"""
        robot = FlierRobot()
        
        assert robot.health == 150
        assert robot.speed == 2.5
        assert robot.ai_level == 5
        assert isinstance(robot, Enemy)
    
    def test_flier_enemy_behavior(self):
        """Test que verifica el comportamiento de enemigos voladores"""
        ghost = FlierGhost()
        zombie = FlierZombie()
        robot = FlierRobot()
        
        # Verificar que los métodos retornan strings
        assert isinstance(ghost.attack(), str)
        assert isinstance(zombie.move(), str)
        assert isinstance(robot.special_ability(), str)
        
        # Verificar que contienen información específica
        assert "aire" in ghost.attack()
        assert "vuela" in zombie.move()
        assert "vuela" in robot.special_ability()


class TestBossEnemies:
    """Tests para enemigos jefes"""
    
    def test_boss_ghost_attributes(self):
        """Test que verifica los atributos del fantasma jefe"""
        ghost = BossGhost()
        
        assert ghost.health == 120
        assert ghost.speed == 2.0
        assert ghost.ai_level == 6
        assert isinstance(ghost, Enemy)
    
    def test_boss_zombie_attributes(self):
        """Test que verifica los atributos del zombi jefe"""
        zombie = BossZombie()
        
        assert zombie.health == 200
        assert zombie.speed == 1.2
        assert zombie.ai_level == 5
        assert isinstance(zombie, Enemy)
    
    def test_boss_robot_attributes(self):
        """Test que verifica los atributos del robot jefe"""
        robot = BossRobot()
        
        assert robot.health == 300
        assert robot.speed == 1.8
        assert robot.ai_level == 7
        assert isinstance(robot, Enemy)
    
    def test_boss_enemy_behavior(self):
        """Test que verifica el comportamiento de enemigos jefes"""
        ghost = BossGhost()
        zombie = BossZombie()
        robot = BossRobot()
        
        # Verificar que los métodos retornan strings
        assert isinstance(ghost.attack(), str)
        assert isinstance(zombie.move(), str)
        assert isinstance(robot.special_ability(), str)
        
        # Verificar que contienen información específica
        assert "devastador" in ghost.attack()
        assert "autoridad" in zombie.move()
        assert "convocar" in robot.special_ability()


class TestEnemyFactories:
    """Tests para las factories de enemigos"""
    
    def test_ghost_factory(self):
        """Test que verifica que GhostFactory crea fantasmas correctamente"""
        factory = GhostFactory()
        
        wheel_chair_ghost = factory.create_wheel_chair_enemy()
        flier_ghost = factory.create_flier_enemy()
        boss_ghost = factory.create_boss_enemy()
        
        assert isinstance(wheel_chair_ghost, WheelChairGhost)
        assert isinstance(flier_ghost, FlierGhost)
        assert isinstance(boss_ghost, BossGhost)
        
        assert isinstance(wheel_chair_ghost, Enemy)
        assert isinstance(flier_ghost, Enemy)
        assert isinstance(boss_ghost, Enemy)
    
    def test_zombie_factory(self):
        """Test que verifica que ZombieFactory crea zombis correctamente"""
        factory = ZombieFactory()
        
        wheel_chair_zombie = factory.create_wheel_chair_enemy()
        flier_zombie = factory.create_flier_enemy()
        boss_zombie = factory.create_boss_enemy()
        
        assert isinstance(wheel_chair_zombie, WheelChairZombie)
        assert isinstance(flier_zombie, FlierZombie)
        assert isinstance(boss_zombie, BossZombie)
        
        assert isinstance(wheel_chair_zombie, Enemy)
        assert isinstance(flier_zombie, Enemy)
        assert isinstance(boss_zombie, Enemy)
    
    def test_robot_factory(self):
        """Test que verifica que RobotFactory crea robots correctamente"""
        factory = RobotFactory()
        
        wheel_chair_robot = factory.create_wheel_chair_enemy()
        flier_robot = factory.create_flier_enemy()
        boss_robot = factory.create_boss_enemy()
        
        assert isinstance(wheel_chair_robot, WheelChairRobot)
        assert isinstance(flier_robot, FlierRobot)
        assert isinstance(boss_robot, BossRobot)
        
        assert isinstance(wheel_chair_robot, Enemy)
        assert isinstance(flier_robot, Enemy)
        assert isinstance(boss_robot, Enemy)
    
    def test_factory_abstract_class(self):
        """Test que verifica que EnemyFactory es una clase abstracta"""
        with pytest.raises(TypeError):
            EnemyFactory()


class TestEnemyHierarchy:
    """Tests para verificar la jerarquía de herencia"""
    
    def test_wheel_chair_enemy_hierarchy(self):
        """Test que verifica la jerarquía de enemigos en silla de ruedas"""
        ghost = WheelChairGhost()
        zombie = WheelChairZombie()
        robot = WheelChairRobot()
        
        # Verificar que heredan de Enemy
        assert isinstance(ghost, Enemy)
        assert isinstance(zombie, Enemy)
        assert isinstance(robot, Enemy)
        
        # Verificar que heredan de Enemy
        assert isinstance(ghost, Enemy)
        assert isinstance(zombie, Enemy)
        assert isinstance(robot, Enemy)
    
    def test_flier_enemy_hierarchy(self):
        """Test que verifica la jerarquía de enemigos voladores"""
        ghost = FlierGhost()
        zombie = FlierZombie()
        robot = FlierRobot()
        
        # Verificar que heredan de Enemy
        assert isinstance(ghost, Enemy)
        assert isinstance(zombie, Enemy)
        assert isinstance(robot, Enemy)
        
        # Verificar que heredan de Enemy
        assert isinstance(ghost, Enemy)
        assert isinstance(zombie, Enemy)
        assert isinstance(robot, Enemy)
    
    def test_boss_enemy_hierarchy(self):
        """Test que verifica la jerarquía de enemigos jefes"""
        ghost = BossGhost()
        zombie = BossZombie()
        robot = BossRobot()
        
        # Verificar que heredan de Enemy
        assert isinstance(ghost, Enemy)
        assert isinstance(zombie, Enemy)
        assert isinstance(robot, Enemy)
        
        # Verificar que heredan de Enemy
        assert isinstance(ghost, Enemy)
        assert isinstance(zombie, Enemy)
        assert isinstance(robot, Enemy)


class TestEnemyStats:
    """Tests para verificar las estadísticas de los enemigos"""
    
    def test_health_comparison(self):
        """Test que verifica que los jefes tienen más salud"""
        wheel_chair_ghost = WheelChairGhost()
        flier_ghost = FlierGhost()
        boss_ghost = BossGhost()
        
        # Los jefes deben tener más salud
        assert boss_ghost.health > wheel_chair_ghost.health
        assert boss_ghost.health > flier_ghost.health
    
    def test_speed_comparison(self):
        """Test que verifica que los voladores son más rápidos"""
        wheel_chair_zombie = WheelChairZombie()
        flier_zombie = FlierZombie()
        boss_zombie = BossZombie()
        
        # Los voladores deben ser más rápidos
        assert flier_zombie.speed > wheel_chair_zombie.speed
        assert flier_zombie.speed > boss_zombie.speed
    
    def test_ai_level_comparison(self):
        """Test que verifica que los robots tienen mejor IA"""
        wheel_chair_robot = WheelChairRobot()
        flier_robot = FlierRobot()
        boss_robot = BossRobot()
        
        # Los robots deben tener mejor IA
        assert boss_robot.ai_level > wheel_chair_robot.ai_level
        assert flier_robot.ai_level > wheel_chair_robot.ai_level


class TestEnemyBehavior:
    """Tests para verificar el comportamiento específico de cada tipo"""
    
    def test_ghost_behavior_patterns(self):
        """Test que verifica patrones de comportamiento de fantasmas"""
        wheel_chair_ghost = WheelChairGhost()
        flier_ghost = FlierGhost()
        boss_ghost = BossGhost()
        
        # Todos los fantasmas deben mencionar "fantasmal" en sus ataques
        assert "fantasmal" in wheel_chair_ghost.attack()
        assert "fantasmal" in flier_ghost.attack()
        assert "fantasmal" in boss_ghost.attack()
    
    def test_zombie_behavior_patterns(self):
        """Test que verifica patrones de comportamiento de zombis"""
        wheel_chair_zombie = WheelChairZombie()
        flier_zombie = FlierZombie()
        boss_zombie = BossZombie()
        
        # Todos los zombis deben mencionar "mordiscos" en sus ataques
        assert "mordiscos" in wheel_chair_zombie.attack()
        assert "mordiscos" in flier_zombie.attack()
        assert "mordiscos" in boss_zombie.attack()
    
    def test_robot_behavior_patterns(self):
        """Test que verifica patrones de comportamiento de robots"""
        wheel_chair_robot = WheelChairRobot()
        flier_robot = FlierRobot()
        boss_robot = BossRobot()
        
        # Todos los robots deben mencionar "láseres" en sus ataques
        assert "láseres" in wheel_chair_robot.attack()
        assert "láseres" in flier_robot.attack()
        assert "láseres" in boss_robot.attack()


class TestFactoryMethodNames:
    """Tests para verificar que los métodos de factory tienen los nombres correctos"""
    
    def test_ghost_factory_methods(self):
        """Test que verifica los métodos de GhostFactory"""
        factory = GhostFactory()
        
        # Verificar que los métodos existen y tienen los nombres correctos
        assert hasattr(factory, 'create_wheel_chair_enemy')
        assert hasattr(factory, 'create_flier_enemy')
        assert hasattr(factory, 'create_boss_enemy')
        
        # Verificar que los métodos son callable
        assert callable(factory.create_wheel_chair_enemy)
        assert callable(factory.create_flier_enemy)
        assert callable(factory.create_boss_enemy)
    
    def test_zombie_factory_methods(self):
        """Test que verifica los métodos de ZombieFactory"""
        factory = ZombieFactory()
        
        # Verificar que los métodos existen y tienen los nombres correctos
        assert hasattr(factory, 'create_wheel_chair_enemy')
        assert hasattr(factory, 'create_flier_enemy')
        assert hasattr(factory, 'create_boss_enemy')
        
        # Verificar que los métodos son callable
        assert callable(factory.create_wheel_chair_enemy)
        assert callable(factory.create_flier_enemy)
        assert callable(factory.create_boss_enemy)
    
    def test_robot_factory_methods(self):
        """Test que verifica los métodos de RobotFactory"""
        factory = RobotFactory()
        
        # Verificar que los métodos existen y tienen los nombres correctos
        assert hasattr(factory, 'create_wheel_chair_enemy')
        assert hasattr(factory, 'create_flier_enemy')
        assert hasattr(factory, 'create_boss_enemy')
        
        # Verificar que los métodos son callable
        assert callable(factory.create_wheel_chair_enemy)
        assert callable(factory.create_flier_enemy)
        assert callable(factory.create_boss_enemy)


if __name__ == "__main__":
    # Ejecutar los tests con pytest
    pytest.main([__file__, "-v"])
