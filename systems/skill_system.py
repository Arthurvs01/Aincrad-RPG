import random


class SkillSystem:

    # =========================
    # REGENERAÇÃO
    # =========================
    @staticmethod
    def regeneration(player, max_hp):
        level = player.skills.get("regeneracao", 0)
        if level == 0:
            return 0

        return int(max_hp * (0.02 * level))


    # =========================
    # BONUS % ATAQUE
    # =========================
    @staticmethod
    def attack_bonus(player, base_atk):
        level = player.skills.get("atk_percent", 0)
        return int(base_atk * (0.05 * level))


    # =========================
    # BONUS % DEFESA
    # =========================
    @staticmethod
    def defense_bonus(player, base_def):
        level = player.skills.get("def_percent", 0)
        return int(base_def * (0.05 * level))


    # =========================
    # ROUBO DE VIDA
    # =========================
    @staticmethod
    def lifesteal(player, damage_dealt):
        level = player.skills.get("roubo_vida", 0)
        return int(damage_dealt * (0.03 * level))


    # =========================
    # FORTUNA (DROP BONUS)
    # =========================
    @staticmethod
    def fortune(player):
        level = player.skills.get("fortuna", 0)
        return level * 2  # +2% por nível


    # =========================
    # CRÍTICO
    # =========================
    @staticmethod
    def critical_hit(player):
        level = player.skills.get("critico", 0)
        chance = level * 3  # 3% por nível
        return random.randint(1, 100) <= chance


    # =========================
    # ESQUIVA
    # =========================
    @staticmethod
    def dodge(player):
        level = player.skills.get("esquiva", 0)
        chance = level * 2  # 2% por nível
        return random.randint(1, 100) <= chance


    # =========================
    # RESISTÊNCIA (% redução de dano)
    # =========================
    @staticmethod
    def resistance(player, incoming_damage):
        level = player.skills.get("resistencia", 0)
        reduction = incoming_damage * (0.02 * level)
        return int(incoming_damage - reduction)


    # =========================
    # PRECISÃO (ignora defesa)
    # =========================
    @staticmethod
    def precision_ignore_def(player):
        level = player.skills.get("precisao", 0)
        return level * 1  # ignora 1 defesa por nível


    # =========================
    # INSTINTO (ataque duplo)
    # =========================
    @staticmethod
    def double_attack(player):
        level = player.skills.get("instinto", 0)
        chance = level * 2  # 2% por nível
        return random.randint(1, 100) <= chance


    # =========================
    # FOCO (aumenta chance geral de skill)
    # =========================
    @staticmethod
    def focus_bonus(player):
        level = player.skills.get("foco", 0)
        return level * 2  # +2% chance global