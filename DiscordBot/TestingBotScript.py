import discord
import os
import sys
from datetime import datetime
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(datetime.now())



licenseFile = open('testBOT.txt', 'r')
botLicense = licenseFile.readline()
client.run(botLicense)