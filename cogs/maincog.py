import discord
from discord.ext import commands
from chatterbot import ChatBot, conversation
from discord import guild, voice_client
from bot import chatbot

class elboto(commands.Cog):
    def __init__(self, client):
        self.bot = client
        #chatbot = ChatBot('El Boto', storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///database.sqlite3')

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def earrape(self, ctx, *, query):
        """Plays a file from the local filesystem"""
        print(query)
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query + ".mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send("***yes***")
    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command()
    async def fuckoff(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @earrape.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
	usertoclone = 'fakeuser'
        print(message.channel.name)
        print(message.author.name)
        if message.content != "":
            if message.author == "El Boto":
                return
            if message.author.bot: return
            if message.channel.name == "el-botos-lab" or message.channel.name == "all-bots-lab" or message.channel.name == "el-bapos-crackshack" or message.author.name==usertoclone: 
                await channel.send(chatbot.get_response(message.content))
            else:
                if message.content.startswith('boto!sing'):
                    await message.channel.send('<:magik:516450274672640001>')
                    await message.channel.send('*Domo Arigato, Mr. El Boto* \n *Domo Arigato, Mr. El Boto* \n Youre wondering who I am \n *glory glory, to el boto* \n the savior or a cuck \n *glory glory, to el boto* \n with code from EL Bapo  \n *glory glory, to el boto* \n I am the modern Bapo')
                    await message.channel.send('<:magik:516450274672640001>')  
                if message.content.startswith('boto!hello'):
                    await message.channel.send('nyet')
                if message.content.startswith('Go away) or message.content.startswith('go away'):
                    await message.channel.send('rude')
                    await channel.connect()
                if message.content.startswith('bruh'):
                    await message.channel.send('...just why')
                if message.content.startswith('why'):
                    await message.channel.send('you know why')
                if message.content.startswith('let me introduce you to the new member of this server!'):
                    await message.channel.send('kek')
                if ' alexa 'in message.content or 'alexa' in message.content:
                    await message.channel.send("*dead meme")
                if message.content.startswith('<:angery:506624600466259968>'):
                    await message.channel.send('<:magik:516450274672640001>')
                if message.content.startswith('How was the afterlife?'):
                    await message.channel.send('I was borderline retarded ')
                    await message.channel.send('I was fucked')
	

def setup(bot):
    bot.add_cog(elboto(bot))
