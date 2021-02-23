# El-Boto
A fun and simple discord bot utilizing chatterbot to create a chatbot that responds to any message in a channel called "el botos lab" or from simple preset responses in any channel.


HOW TO RUN EL BOTO:
1. Make sure you have chatterbot, discordpy, chatterbot-corpus, and python 3.7(new versions WILL NOT work) installed
3. If you intend to use El Boto to create a chatbot from a discord user's messages, create a csv file from discordchatexporter and rename the file to "boltresponses.csv". The Aquire-data.py script will then seperate the csv into seperate response and stimulus files. The accuracy of a bot made using this method will not be high.
4. Make sure to create a new bot on the discord developer panel, then add that bot's token to the bottom of "bot.py"
5. if you wish to have EL Boto respond to specific person outside of the "el botos lab" channel besides the preset messages, you may uncomment the lines in the main cog and fill in the user ID.
6. After all this, simply run "bot.py" and enjoy.
OPTIONAL
If you want El Boto to play music in the voice chat, include the audio file in .mp3 format. Make sure ffmpeg is installed and you should be ready to go.
