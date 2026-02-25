import random
from core.attribute_calc import AttributeCalculator
from core.skill_system import SkillSystem


class CombatSystem:

    @staticmethod
    def calculate_damage(attacker, defender, attacker_stats, defender_stats):

        # =========================
        # Precisão (ignora defesa)
        # =========================
        ignore_def = SkillSystem.precision_ignore_def(attacker)
        effective_def = max(0, defender_stats["defesa"] - ignore_def)

        # =========================
        # Dano base
        # =========================
        damage = attacker_stats["ataque"] - effective_def
        damage = max(1, damage)

        # =========================
        # Crítico
        # =========================
        if SkillSystem.critical_hit(attacker):
            damage = int(damage * 1.5)
            crit = True
        else:
            crit = False

        # =========================
        # Resistência do defensor
        # =========================
        damage = SkillSystem.resistance(defender, damage)

        return damage, crit


    @staticmethod
    def fight(player, enemy):

        player_stats = AttributeCalculator.calculate(player)
        enemy_stats = AttributeCalculator.calculate(enemy)

        player_hp = player_stats["vida"]
        enemy_hp = enemy_stats["vida"]

        log = []

        # =========================
        # Ordem de turno (velocidade)
        # =========================
        player_turn = player_stats["velocidade"] >= enemy_stats["velocidade"]

        while player_hp > 0 and enemy_hp > 0:

            if player_turn:

                # Esquiva do inimigo
                if SkillSystem.dodge(enemy):
                    log.append("💨 Inimigo esquivou!")
                else:
                    damage, crit = CombatSystem.calculate_damage(
                        player, enemy, player_stats, enemy_stats
                    )

                    enemy_hp -= damage
                    log.append(f"⚔️ Você causou {damage} de dano.")

                    if crit:
                        log.append("🔥 CRÍTICO!")

                    # Roubo de vida
                    steal = SkillSystem.lifesteal(player, damage)
                    player_hp += steal
                    if steal > 0:
                        log.append(f"🩸 Você recuperou {steal} de vida.")

                    # Ataque duplo
                    if SkillSystem.double_attack(player):
                        enemy_hp -= damage
                        log.append("⚡ Ataque duplo ativado!")

                # Regeneração
                regen = SkillSystem.regeneration(player, player_stats["vida"])
                if regen > 0:
                    player_hp += regen
                    log.append(f"✨ Regeneração curou {regen}.")

            else:

                # Esquiva do jogador
                if SkillSystem.dodge(player):
                    log.append("💨 Você esquivou!")
                else:
                    damage, crit = CombatSystem.calculate_damage(
                        enemy, player, enemy_stats, player_stats
                    )

                    player_hp -= damage
                    log.append(f"🗡 Inimigo causou {damage} de dano.")

                    if crit:
                        log.append("💀 Inimigo causou CRÍTICO!")

                # Regeneração inimigo
                regen = SkillSystem.regeneration(enemy, enemy_stats["vida"])
                if regen > 0:
                    enemy_hp += regen

            player_turn = not player_turn

        winner = "player" if player_hp > 0 else "enemy"

        return {
            "winner": winner,
            "log": log,
            "player_remaining_hp": max(0, player_hp),
            "enemy_remaining_hp": max(0, enemy_hp)
        }