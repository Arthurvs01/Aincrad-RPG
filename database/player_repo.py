import os
import json

BASE_PATH = "database/data/players/"


class PlayerRepository:

    def _get_filepath(self, character_name: str, chat_id: int):
        filename = f"{character_name}-{chat_id}.json"
        return os.path.join(BASE_PATH, filename)

    def player_exists(self, chat_id: int):
        for file in os.listdir(BASE_PATH):
            if file.endswith(f"-{chat_id}.json"):
                return True
        return False

    def create_player(self, player):
        filepath = self._get_filepath(player.character_name, player.chat_id)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(player.to_dict(), f, indent=4)

    def get_player_by_chat_id(chat_id: int):
        for file in os.listdir(BASE_PATH):
            if file.endswith(f"-{chat_id}.json"):
                with open(os.path.join(BASE_PATH, file), "r", encoding="utf-8") as f:
                    return json.load(f)
        return None
