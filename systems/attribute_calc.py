class AttributeCalculator:

    @staticmethod
    def calculate(player):
        """
        Retorna os atributos finais de combate
        """

        # =========================
        # Base
        # =========================
        base_hp = player.hp
        base_atk = player.atk
        base_def = player.defense
        base_agi = player.agi

        # =========================
        # Buffs de Equipamento
        # =========================
        bonus_hp = 0
        bonus_atk = 0
        bonus_def = 0
        bonus_agi = 0

        for item in player.equipped.values():
            if item:
                bonus_hp += item.get("hp_bonus", 0)
                bonus_atk += item.get("atk_bonus", 0)
                bonus_def += item.get("def_bonus", 0)
                bonus_agi += item.get("agi_bonus", 0)

        # =========================
        # Atributos Finais
        # =========================

        final_hp = (base_hp + bonus_hp) * 3
        final_atk = base_atk + bonus_atk
        final_def = base_def + bonus_def
        final_speed = int((base_agi + bonus_agi) / 2)

        return {
            "vida": final_hp,
            "ataque": final_atk,
            "defesa": final_def,
            "velocidade": final_speed
        }