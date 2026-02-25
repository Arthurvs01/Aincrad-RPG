from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.message_manager import MessageManager
from core.text_loader import TextLoader

async def floor_1(update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    keyboard = [
        [
            InlineKeyboardButton("🌲 Floresta", callback_data="floor_1_forest"),
            InlineKeyboardButton("🏙 Cidade", callback_data="floor_1_city"),
        ],
        [
            InlineKeyboardButton("👤 Personagem", callback_data="profile"),
            InlineKeyboardButton("🧭 Viajar", callback_data="travel"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await MessageManager.send_or_edit(
        update,
        context,
        text=TextLoader.load("floors/floor_1.txt"),
        image_path="floors/floor_1/floor_1.jpg",
        reply_markup=reply_markup,
    )