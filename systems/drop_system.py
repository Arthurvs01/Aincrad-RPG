import random


class DropSystem:

    @staticmethod
    def forest_drops(mob_level):

        drops = {}

        # =====================
        # Ouro (escala com nível)
        # =====================
        gold = random.randint(5 * mob_level, 15 * mob_level)
        drops["ouro"] = gold

        # =====================
        # Couro (30%)
        # =====================
        if random.random() <= 0.30:
            drops["couro"] = 1

        # =====================
        # Joia de Vida (3%)
        # =====================
        if random.random() <= 0.03:
            drops["joia_vida"] = 1

        return drops