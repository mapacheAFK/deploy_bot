from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Tu token de bot de Telegram
TOKEN = '6831459039:AAEBVkDiYm0BfrK5NmgE4mbTOE89_1YNuqg'
# Tu ID de chat (obtenido de @myidbot)
ADMIN_CHAT_ID = 6170415076  # Asegúrate de usar un entero, no una cadena de texto

async def start(update: Update, context: CallbackContext) -> None:
    """Envía un mensaje cuando el comando /start es emitido."""
    await update.message.reply_text('Hola! Estoy escuchando tus mensajes.')

async def forward_message(update: Update, context: CallbackContext) -> None:
    """Reenvía todos los mensajes que recibe el bot al chat del administrador."""
    await context.bot.forward_message(chat_id=ADMIN_CHAT_ID,
                                      from_chat_id=update.message.chat_id,
                                      message_id=update.message.message_id)

def main() -> None:
    """Inicia el bot."""
    application = Application.builder().token(TOKEN).build()

    # Comandos manejadores
    application.add_handler(CommandHandler("start", start))

    # Manejador de mensajes
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    main()
