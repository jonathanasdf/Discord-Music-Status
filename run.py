#!/usr/local/bin/python3
import discord
from discord.ext import commands
import asyncio
import configparser
from functools import partial
import logging
logging.basicConfig(level=logging.INFO)
print = partial(print, flush=True)


config = configparser.ConfigParser()
config.read("config.ini")
try:
    token = config['Config']['token']
except KeyError:
    print("Please assign your token in config.ini")
    input()
if token == "":
    print("Please assign your token in config.ini")
    input()
try:
    snip = config['Config']['snip']
except KeyError:
    print("Please assign your snip directory in config.ini")
    input()
if token == "":
    print("Please assign your token in config.ini")
    input()

# Set's bot's desciption and prefixes in a list
description = ""
bot = commands.Bot(command_prefix=['musicself.'], description=description, self_bot=True)

###################
## Startup Stuff ##
###################

bot.remove_command('help')

@bot.event
async def on_ready():
    # Outputs login data to console
    print("---------------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("---------------------------")
    savesong = "_____________"
    while True:
        song = pull_song()
        song = song[:song.rfind('[')-1]
        if savesong != song:
            savesong = song
            if song.strip() == '':
                await bot.change_presence(game=discord.Game())
                print("Stopped playing music.")
            else:
                await bot.change_presence(game=discord.Game(name=song))
                print("Listening to: {}".format(song))
        await asyncio.sleep(1)

@bot.event
async def on_message(message):
    if message.content == "!np":
        song = pull_song()
        if song.strip() == '':
            await bot.send_message(message.channel, "```css\nNot listening to anything!```")
        else:
            await bot.send_message(message.channel, "```css\nListening to: {}```".format(song))
            yt_message = await bot.send_message(message.channel, "~yt {}".format(song))
            await bot.delete_message(yt_message)
    await bot.process_commands(message)

def pull_song():
    # $if(%ispaused%,,
    # $if(%artist%,%artist% - ,$if(%album%,%album% - ))
    # %title%
    # )
    file = open(snip, encoding="utf8")
    song = file.read()
    return song

##############################
## FANCY TOKEN LOGIN STUFFS ##
##############################

try:
    bot.run(token, bot=False)
except discord.errors.LoginFailure:
    print("Invalid token")
