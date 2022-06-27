class Zombie:
    """Creates zombies
    """
    # constructor for th zombie object

    def __init__(self, health=100.0: float, damage=10: float):
        """Constructor for creating zombie instances/objects
        Args:
        health (float): The starting health of the zombie
        damage (float): The starting damage of the zombie
        """
        self.__health = health
        self.__damage = damage
    # returns the health of the current zombie object

    def getHealth(self) -> float:
        return self.__health

    # returns the damage the current zombie object/instance deals
    def getDamage(self) -> float:
        return self.__damage

    # sets the health of the current zombie object/instance
    def setHealth(self, newhealth: float):
        self.__health = newhealth

    # sets the current damage of the zombie object/instace
    def setDamage(self, newDamage: float):
        self.__damage = newDamage

    # Subtracks damage taken from remaning health
    def damageTaken(damageTaken):
        if damageTaken < getHealth:
            setHealth -= damageTaken
        else:
            print("Zombie died!")
