import discord
import os
from replit import db
import random

client = discord.Client()

quotes = [
  "This *does* compute!",
  "Check, please.",
  "My alarm says it's time for Finn's bath. Finn, get naked.",
  "Sure he's a dirt bag born out of a mother, but who's not?",
  "My face! Finn! Jake! Kiss my face!",
  "I think I am dying. But that's okay, BMO always bounces back!",
  "You are so beautiful and I love you.",
  "She is red hot like pizza supper.",
  "If anyone tries to hurt Finn, I will kill them.",
  "What if I put some knuckle in your eyeballs? Would that help you think?",
  "Jake, you drive a hard burger."
  "I'm learning truth about myself."
]

dota_quotes = [
  "Who wants to play video games?",
  "If I push this button, you will both be dangerously transported into my main brain game frame, where it is very dangerous.",
  "No! It's a far-too-dangerous incredible adventure for you! That's final.",
  "No, I do not play such games... with Jake.",
  "BMO Chop! If this were a real attack, you'd be dead.",
  "NO! NOT TODAY! NOO CARD WAARR—"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')

    if message.content.startswith('$remind'):
      await message.channel.send('What would you like your reminder to be?')

    if message.content.startswith('$quote'):
      await message.channel.send(random.choice(quotes))
      
    if message.content == '@DotAs':
      await message.channel.send(random.choice(dota_quotes))


client.run(os.getenv('TOKEN'))
