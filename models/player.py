class Player:
    def __init__(self, chat_id: int, character_name: str, player_class: str, stats: dict):
        self.chat_id = chat_id
        self.character_name = character_name
        self.player_class = player_class

        # Progressão
        self.level = 1
        self.xp = 0

        # Atributos base
        self.hp = stats["hp"]
        self.atk = stats["atk"]
        self.defense = stats["def"]
        self.agi = stats["agi"]

        # Economia
        self.gold = 0

        # Mundo
        self.floor = 1
        self.guild_id = None
        self.death = 0

        # Inventário estruturado
        self.inventory = {
            "items": {
                "gold": 0,
                "couro": 0,
                "madeira": 0,
                "aco": 0,
                "linha": 0,
                "jewel_life": 0,
                "jewel_upgrade": 0,
            },
            "equipment": {
                "weapon": [],
                "helmet": [],
                "armor": [],
                "pants": [],
                "boots": []
            },
            "tools": {
                "axe": [],
                "pickaxe": [],
                "scissors": []
            }
        }

        # Equipados atualmente
        self.equipped = {
            "weapon": None,
            "helmet": None,
            "armor": None,
            "pants": None,
            "boots": None
        }

        # Skills
        self.skills = {
            "regeneracao": 0,
            "atk_percent": 0,
            "def_percent": 0,
            "roubo_vida": 0,
            "fortuna": 0,
            "critico": 0,
            "esquiva": 0,
            "resistencia": 0,
            "precisao": 0,
            "instinto": 0,
            "foco": 0
        }

    def to_dict(self):
        return self.__dict__
