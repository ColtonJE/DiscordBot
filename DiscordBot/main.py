import discord
from datetime import datetime
from time import sleep

client = discord.Client()


async def timed_message():
    while 929:
        dt = datetime.now()
        if( dt.hour == 9 and dt.minute == 29 ):
            channel = client.get_channel(649454038483468318)
            ethanid = '<@356881123088793600>'
            # userid = '<@278375594079551488>'

            await channel.send('Hey look %s its 9:29' % ethanid )
        sleep(60)
#piss piss penis
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.loop.create_task(timed_message())
    print(datetime.now())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTEwOTcyNzcwMjc4NjA0ODcx.YZangQ.ANjGvcrW9R4Z0LIJblwNToXsKnU')
