import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$remind'):
        await message.channel.send('What would you like your reminder to be?')

        discord.on_message(message):
          

client.run(os.getenv('TOKEN'))
