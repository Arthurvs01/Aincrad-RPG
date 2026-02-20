from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.message_manager import MessageManager

async def exemplo_menu(update, context):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

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
        text="floors/floor_",
        image_path="floors/floor_.png",
        reply_markup=reply_markup,
    )