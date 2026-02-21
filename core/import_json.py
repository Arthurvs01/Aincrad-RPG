import os
class TextLoader:
    BASE_PATH = "database/data/players"
    @staticmethod
    def load_json(username: str, chat_id: str):
        filename = f"{username}-{chat_id}.json"
        path = os.path.join(TextLoader.BASE_PATH, filename)

        with open(path, "r", encoding="utf-8") as f:
            return f.read()