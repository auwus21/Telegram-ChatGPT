import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

# Configuración de la clave de API de OpenAI
openai.api_key = "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"

# Manejador de comandos
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy un bot de prueba.")

# Manejador de mensajes
def echo(update, context):
    message = update.message.text
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=message,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7,
            model="text-davinci-002",
            frequency_penalty=0,
            presence_penalty=0,
            response_format="json",
            endpoint="https://api.openai.com/v1/chat/completions"
        )
        context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)
    except openai.Error as e:
        print("OpenAI Error:", e)

# Configuración del token de acceso del bot
TOKEN = "6032272152:AAG2AyBCes2-g_5ZnJuyVUvhkN0PAiNDrmQ"
updater = Updater(token=TOKEN, use_context=True)

# Creación de manejadores de comandos y mensajes
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

# Inicio del bot
updater.start_polling()
updater.idle()

#hola
