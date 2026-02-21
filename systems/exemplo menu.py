from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.message_manager import MessageManager
from core.text_loader import TextLoader
from database.player_repo import PlayerRepository

async def exemplo_menu(update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    dados = PlayerRepository.get_player_by_chat_id(chat_id)
    name = dados["character_name"]

    keyboard = [
        [
            InlineKeyboardButton("AAA", callback_data="AAA"),
            InlineKeyboardButton("AAA", callback_data="AAA"),
        ],
        [
            InlineKeyboardButton("AAA", callback_data="AAA"),
            InlineKeyboardButton("AAA", callback_data="AAA"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await MessageManager.send_or_edit(
        update,
        context,
        text=TextLoader.load("caminho.txt").format(),
        image_path="caminho.png",
        reply_markup=reply_markup,
    )