import discord
from discord.utils import get
from discord.ext import commands
from discord.voice_client import VoiceClient
import re
import logging 
#load_opus_lib()
from chatterbot import ChatBot, conversation
from chatterbot.trainers import ListTrainer
from discord import guild, voice_client
from email import message

chatbot = ChatBot('El Boto', storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
chatbot.storage.drop()
trainer = ListTrainer(chatbot)
data = open('training-data.txt').read()
conversations = data.strip().split('\n')
trainer.train(conversations)
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="el boto")
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)
 #train bot
channel = client.get_channel(590997905951948800) 
text_channel_list = client.guilds
print(text_channel_list)

client.load_extension("cogs.maincog")
#client.add_cog(elboto(client))
client.run('NTg4MTA5Mzg3MTgxMDY0MjAw.XZEijQ.UC69aulAv4ydImg52kgnbckDmiQ')
