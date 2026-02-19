from telegram import Update
from telegram.ext import ContextTypes


class CallbackRouter:

    def __init__(self):
        self.routes = {}

    def register(self, key: str, handler):
        """
        key pode ser:
        - valor exato: "create_character"
        - prefixo: "class_"
        """
        self.routes[key] = handler

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        query = update.callback_query
        await query.answer()

        data = query.data

        for key, handler in self.routes.items():
            if data == key or data.startswith(key):
                return await handler(update, context)

        # fallback opcional
        await query.answer("Ação inválida.", show_alert=True)
