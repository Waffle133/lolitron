import discord
from settings import get_bot_token
from discord.ext import commands

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Bot is ready')

client.run(get_bot_token())

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))
#
#
# client = MyClient()
# client.run('NDc3MTc3ODc5NDU3ODI0Nzcw.Xm7hVg.YuYasGAHdCrdZoSxMdj6x_B0caA')
