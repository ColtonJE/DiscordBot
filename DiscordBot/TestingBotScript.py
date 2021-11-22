import asyncio

import discord
from discord.ext import tasks, commands
import os
import sys
from datetime import datetime
from time import sleep

client = discord.Client()


async def annoyEthan():
    while 929:
        if datetime.now().minute == 29 and datetime.now().hour == 9:
            channels = client.get_all_channels()
            ethanid = '<@356881123088793600>'
            channel = client.get_channel(649451080689778731)
            for guild in client.guilds:
                for channel in guild.channels:
                    if channel.name == 'el-generalmente':
                        await channel.send("Hey look %s its 9:29 :partying_face:" % ethanid)
            # await channel.send("Hey look %s its 9:29 :partying_face:" % ethanid)
            print("it is time")
        await asyncio.sleep(60)

client.loop.create_task(annoyEthan())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(datetime.now())
    text_channel_list = []
    # print(client.guilds.)
    # for guild in client.guilds:
    #     for channel in guild.channels:
    #         text_channel_list.append(channel)
    # chancat = text_channel_list[0]
    # sendchan = client.get_channel(chancat.id)
    # await sendchan.send("ugh")
    channel = discord.Object(id='649451080689778731')
    await channel.send("ugh")
    print(text_channel_list)





licenseFile = open('testBOT.txt', 'r')
botLicense = licenseFile.readline()
client.run(botLicense)