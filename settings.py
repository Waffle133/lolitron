from dotenv import load_dotenv
import os


def get_bot_token():
    load_dotenv()
    bot_token = os.getenv('DISCORD_BOT_TOKEN')
    return bot_token
