import discord
import git
import os
import sys
from datetime import datetime
from time import sleep

client = discord.Client()
g = git.Git('/home/pi/Documents/DiscordBotGoBRRR')

# *
# *
# *  WARNING DO NOT PUT UNTESTED CHANGES IN THIS BOT
# *  THE BOT WILL GO DOWN IF IT ERRORS OUT
# *
# *

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # client.loop.create_task(timed_message())
    print(datetime.now())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        ethanid = '<@356881123088793600>'
        # channel = client.get_channel(649454038483468318)
        await message.channel.send('Hey look %s its 9:29 :partying_face:' % ethanid)
        # await message.channel.send('Hello!')
    #updates the project from the github automatically
    if message.content.startswith('$update'):
        g.pull()
        print("Sucessfully pulled. Restarting now.")
        os.execv(sys.executable, ['python'] + sys.argv)
        sleep(1)
        quit()

licenseFile = open('license.txt', 'r')
botLicense = licenseFile.readline()
client.run(botLicense)

