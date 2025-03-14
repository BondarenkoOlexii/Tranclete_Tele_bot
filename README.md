Telegram Translator Bot


Description

This Telegram bot automatically translates received messages into the user's selected language. It uses googletrans for translation and pyTelegramBotAPI for interaction with Telegram.


Features

Automatic translation of received messages. Default language detection based on the user's Telegram settings.Ability to change the translation language via command.Support for multiple languages.

Installation

Install the required libraries:
pip install pyTelegramBotAPI googletrans==4.0.0-rc1 Obtain a Telegram bot token from BotFather. Replace the Token in the bot's code with your own.

Usage
Run the bot:
python bot.py

Commands

/start – Starts the bot and detects the user's default language.
/language <language_code> – Sets the target translation language.
Example: /language en (English).
/code_language – Displays a list of supported languages.

Supported Languages

🇬🇧 English (en)
🇺🇦 Ukrainian (uk)
🇪🇸 Spanish (es)
🇮🇱 Hebrew (iw)
🇮🇹 Italian (it)
🇮🇳 Hindi (hi)
🇫🇷 French (fr)
🇩🇪 German (de)
🇹🇷 Turkish (tr)
🇯🇵 Japanese (ja)
🇨🇳 Chinese (zh-cn)
🇮🇩 Indonesian (id)

Troubleshooting

If the bot is not working or not translating:

Ensure that the correct version of googletrans (4.0.0-rc1) is installed.
Verify that the Telegram token is correct.
Restart the bot.

Contact

For any suggestions or issues, feel free to reach out. Telegram: https://t.me/Don_t_mssage_me

