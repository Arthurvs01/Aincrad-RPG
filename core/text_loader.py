import os
class TextLoader:
    BASE_PATH = "content/texts/"
    @staticmethod
    def load(filename: str) -> str:
        path = os.path.join(TextLoader.BASE_PATH, filename)

        with open(path, "r", encoding="utf-8") as f:
            return f.read()