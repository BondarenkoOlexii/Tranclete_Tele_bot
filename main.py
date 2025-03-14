import telebot
from googletrans import Translator

Token = ""

bot = telebot.TeleBot(Token)і
trancletor = Translator()

LANGUAGES = {
    'zh-cn': 'chinese (simplified)', 'en': 'english', 'fr': 'french', 'de': 'german', 'hi': 'hindi', 'id': 'indonesian','iw': 'hebrew',
    'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'la': 'latin', 'pl': 'polish', 'ru': 'russian', 'es': 'spanish', 'sv': 'swedish', 'tr': 'turkish', 'uk': 'ukrainian'
}

language_to_tranclete = None

def start_bot(_):
    print("Bot ready for use")


@bot.message_handler(commands=['start'])
def start_button(message):
    global language_to_tranclete
    bot.send_message(message.chat.id, "Hello, this is trancletor bot, all message will tranclete to language on your telegram")
    language_to_tranclete = message.from_user.language_code


@bot.message_handler(commands=['language'])
def help_button(message):
    global language_to_tranclete
    parts = message.text.split()
    if len(parts) > 1:
        lang_code = parts[1].strip().lower()
        if lang_code in LANGUAGES:
            language_to_tranclete = lang_code
            bot.send_message(message.chat.id, f"Language to tranclete changed to {LANGUAGES[lang_code]}.")
        else:
            bot.send_message(message.chat.id, "Unknow language code. Please try again.")
    else:
        bot.send_message(message.chat.id, "Write code of language after command. Like this: /language en")


@bot.message_handler(commands=['code_language'])
def language(message):
    bot.send_message(chat_id=message.chat.id,
    text=f"U can use this language:\n 🇺🇦 : `uk` \n 🇬🇧 : `eg` \n 🇪🇸 : `es` \n 🇮🇱: `iw` \n 🇮🇹 : `it` \n 🇮🇳 : `hi` \n 🇫🇷: `fr` \n 🇩🇪: `de` \n 🇹🇷 : `tr` \n 🇯🇵 : `ja` \n 🇨🇳 : `zh-cn` \n 🇮🇩 : `id`\n",parse_mode="MarkdownV2")

@bot.message_handler(content_types=['text'])
def tranclete_message(message):
    trancleted = trancletor.translate(message.text, dest=language_to_tranclete)
    bot.reply_to(message, trancleted.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)