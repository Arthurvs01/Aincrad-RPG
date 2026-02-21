from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.message_manager import MessageManager
from core.text_loader import TextLoader
from database.player_repo import PlayerRepository

async def character_menu(update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    dados = PlayerRepository.get_player_by_chat_id(chat_id)
    name = dados["character_name"]
    pclass = dados["player_class"]
    guild = dados["guild_id"]
    death = dados["death"]

    keyboard = [
        [
            InlineKeyboardButton("Status", callback_data="status"),
            InlineKeyboardButton("Guilda", callback_data="guild"),
        ],
        [
            InlineKeyboardButton("Inventário", callback_data="inventory"),
            InlineKeyboardButton("Equipamentos", callback_data="equipments"),
        ],
        [
            InlineKeyboardButton("Menu", callback_data="Floor_1"),
            InlineKeyboardButton("Reload", callback_data="profile"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await MessageManager.send_or_edit(
        update,
        context,
        text=TextLoader.load("character_menu/character_menu.txt").format(name=name, pclass=pclass, guild=guild, death=death),
        image_path="character_menu/character_menu.jpg",
        reply_markup=reply_markup,
        )