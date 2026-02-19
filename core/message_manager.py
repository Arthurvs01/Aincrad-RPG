from telegram import InputMediaPhoto, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from core.text_loader import TextLoader


class MessageManager:

    @staticmethod
    async def send_or_edit(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        image_path: str,
        text: str,
        reply_markup: InlineKeyboardMarkup | None = None,
    ):
        """
        Envia ou edita a mensagem principal do jogo.
        Funciona para:
        - Comandos (/start)
        - CallbackQuery (botões)
        """

        # Detecta se veio de botão ou comando
        if update.callback_query:
            query = update.callback_query
            await query.answer()

            chat_id = query.message.chat_id
            message_id = query.message.message_id

        else:
            chat_id = update.effective_chat.id
            message_id = context.user_data.get("last_message_id")

        media = InputMediaPhoto(
            media=open(f"content/images/{image_path}", "rb"),
            caption=TextLoader.load(text),
            parse_mode="HTML"
        )

        # Se já temos mensagem anterior → tenta editar
        if message_id:
            try:
                await context.bot.edit_message_media(
                    chat_id=chat_id,
                    message_id=message_id,
                    media=media,
                    reply_markup=reply_markup
                )

                context.user_data["last_message_id"] = message_id
                return

            except Exception:
                # Se falhar, apaga e envia nova
                try:
                    await context.bot.delete_message(chat_id, message_id)
                except:
                    pass

        # Envia nova mensagem
        message = await context.bot.send_photo(
            chat_id=chat_id,
            photo=open(f"content/images/{image_path}", "rb"),
            caption=TextLoader.load(text),
            parse_mode="HTML",
            reply_markup=reply_markup
        )

        context.user_data["last_message_id"] = message.message_id
