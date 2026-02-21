from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.message_manager import MessageManager
from core.text_loader import TextLoader
from database.player_repo import PlayerRepository
import json

async def character_menu(update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    dados = PlayerRepository.get_player_by_chat_id(chat_id)
    name = dados["character_name"]

    keyboard = [
        [
            InlineKeyboardButton("Status", callback_data="AAA"),
            InlineKeyboardButton("Guilda", callback_data="AAA"),
        ],
        [
            InlineKeyboardButton("Inventário", callback_data="AAA"),
            InlineKeyboardButton("Equipamentos", callback_data="AAA"),
        ],
        [
            InlineKeyboardButton("Menu", callback_data="AAA"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await MessageManager.send_or_edit(
        update,
        context,
        text=TextLoader.load("character_menu/character_menu.txt").format(nome=name),
        image_path="character_menu/character_menu.jpg",
        reply_markup=reply_markup,
        )