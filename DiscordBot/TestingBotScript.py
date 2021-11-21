import discord
import git
import os
import sys
from datetime import datetime
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # client.loop.create_task(timed_message())
    print(datetime.now())



licenseFile = open('license.txt', 'r')
botLicense = licenseFile.readline()
client.run(botLicense)