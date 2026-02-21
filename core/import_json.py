import os
class JsonLoader:
    BASE_PATH = "database/data/players"
    @staticmethod
    def load(chat_id: str):
        filename = f"*-{chat_id}.json"
        path = os.path.join(JsonLoader.BASE_PATH, filename)

        with open(path, "r", encoding="utf-8") as f:
            return f.read()