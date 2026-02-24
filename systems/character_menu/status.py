from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.message_manager import MessageManager
from core.text_loader import TextLoader
from database.player_repo import PlayerRepository

async def status(update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    dados = PlayerRepository.get_player_by_chat_id(chat_id)
    name = dados["character_name"]
    classe = dados["player_class"]
    guild = dados["guild_id"] or "Player Sem Guilda"
    lvl = dados["level"]
    xp = dados["xp"]
    hp = dados["hp"]
    atk = dados["atk"]
    defense = dados["defense"]
    agi = dados["agi"]

    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data="profile"),
            InlineKeyboardButton("Menu", callback_data="floor_1"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await MessageManager.send_or_edit(
        update,
        context,
        text=TextLoader.load("character_menu/status.txt").format(name=name, classe=classe, guild=guild, level=lvl, xp=xp, hp=hp, atk=atk, defense=defense, agi=agi),
        image_path="character_menu/status.jpg",
        reply_markup=reply_markup,
    )