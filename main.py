from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, filters
from config import BOT_TOKEN
from core.callback_router import CallbackRouter
from systems.login_system import start_login, create_character, receive_name, select_class, ASK_NAME

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # =========================
    # Callback Router
    # =========================
    router = CallbackRouter()

    router.register("create_character", create_character)
    router.register("class_", select_class)

    # =========================
    # Conversation (Nome)
    # =========================
    login_conversation = ConversationHandler(
        entry_points=[CommandHandler("start", start_login)],
        states={
            ASK_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, receive_name)
            ],
        },
        fallbacks=[],
        allow_reentry=True,
    )

    app.add_handler(login_conversation)

    # =========================
    # Callback Centralizado
    # =========================
    app.add_handler(CallbackQueryHandler(router.handle))

    print("Aincrad RPG iniciado...")
    app.run_polling()


if __name__ == "__main__":
    main()