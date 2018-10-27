import discord
from discord.ext import commands


client = commands.Bot(command_prefix = ":")

print("Bot is online and ready.")

@client.event
async def on_message(message): ##message logging
  author =  message.author
  content = message.content
  print('{}: {}'.format(author, content))
@client.event
async def on_message_delete(message): ##if user deletes a message the bot will resend the message
  author =  message.author
  content = message.content
  channel = message.channel
  await client.send_message(channel, "{}: {}".format(author, content))
@client.event ##bot status
async def on_ready():
  await client.change_presence(game=discord.Game(name='and Watching Birds'))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Hi'):
        msg = 'Hey {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('kitty are you online'):
        msg = 'Yes :) {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)





client.run("NDY3NzE1MzQwODE0NjQ3Mjk2.DrWiTA.yFQi_A2hXAxUkA7EP9fNGL_ARJg")
