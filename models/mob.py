class Mob:

    def __init__(self, name, level, hp, atk, defense, agi):
        self.name = name
        self.level = level
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.agi = agi

        self.skills = {}  # mobs podem ter skills futuramente

class Floor1Forest:

    @staticmethod
    def get_mobs():

        return [
            Mob("Javali Selvagem", 1, 12, 5, 3, 4),
            Mob("Lobo Cinzento", 1, 10, 6, 2, 6),
            Mob("Goblin Explorador", 2, 15, 7, 4, 5),
            Mob("Urso Jovem", 2, 20, 8, 6, 3),
            Mob("Ent Corrompido", 3, 25, 10, 8, 2),
        ]