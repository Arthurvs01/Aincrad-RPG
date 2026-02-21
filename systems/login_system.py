from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, ConversationHandler
from models.player import Player
from database.player_repo import PlayerRepository
from core.message_manager import MessageManager
from core.text_loader import TextLoader


ASK_NAME = 1

player_repo = PlayerRepository()


CLASSES = {
    "Espadachim": {"hp": 9, "atk": 7, "def": 5, "agi": 4},
    "Tanque": {"hp": 11, "atk": 4, "def": 8, "agi": 2},
    "Assassino": {"hp": 5, "atk": 10, "def": 2, "agi": 8},
    "Arqueiro": {"hp": 6, "atk": 6, "def": 3, "agi": 10},
}


# =========================
# INÍCIO
# =========================

async def start_login(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    if player_repo.player_exists(chat_id):
        await MessageManager.send_or_edit(
            update,
            context,
            image_path="welcome.jpg",
            text=TextLoader.load("already_registered.txt"),
            reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Menu", callback_data="floor_1")]]
                )
        )
        return ConversationHandler.END

    keyboard = [
        [InlineKeyboardButton("Criar Personagem ⚔️", callback_data="create_character")]
    ]

    await MessageManager.send_or_edit(
        update,
        context,
        image_path="welcome.jpg",
        text=TextLoader.load("welcome.txt"),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return ASK_NAME


# =========================
# BOTÃO CRIAR PERSONAGEM
# =========================

async def create_character(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await MessageManager.send_or_edit(
        update,
        context,
        image_path="welcome.jpg",
        text=TextLoader.load("ask_name.txt"),
    )

    return ASK_NAME


# =========================
# RECEBE NOME
# =========================

async def receive_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    character_name = update.message.text.strip()

    context.user_data["character_name"] = character_name

    keyboard = [
        [InlineKeyboardButton("Espadachim ⚔️", callback_data="class_Espadachim")],
        [InlineKeyboardButton("Tanque 🛡️", callback_data="class_Tanque")],
        [InlineKeyboardButton("Assassino 🗡️", callback_data="class_Assassino")],
        [InlineKeyboardButton("Arqueiro 🏹", callback_data="class_Arqueiro")],
    ]

    await MessageManager.send_or_edit(
        update,
        context,
        image_path="welcome.jpg",
        text=TextLoader.load("choose_class.txt"),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return ConversationHandler.END


# =========================
# ESCOLHA DE CLASSE
# =========================

async def select_class(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    data = query.data

    chosen_class = data.replace("class_", "")

    character_name = context.user_data.get("character_name")
    chat_id = query.message.chat_id

    stats = CLASSES[chosen_class]

    player = Player(chat_id, character_name, chosen_class, stats)
    player_repo.create_player(player)

    await MessageManager.send_or_edit(
        update,
        context,
        image_path="welcome.jpg",
        text=TextLoader.load("login_success.txt"),
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Menu", callback_data="floor_1")]]
            )
    )

    return ConversationHandler.END
