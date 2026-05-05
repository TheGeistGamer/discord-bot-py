import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

import meme

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def hello(self, message):
    await message.channel.send("Hello World!")

  async def ping(self, message):
    await message.channel.send("Pong!")

  async def meme(self, message):
    await message.channel.send(meme.get())

  async def on_message(self, message):
    if message.author == self.user: return

    commands = {
      "$hello": self.hello,
      "$ping": self.ping,
      "$meme": self.meme
    }

    cmd = message.content.split()[0]

    if cmd in commands:
      await commands[cmd](message)
  
  async def on_member_join(self, member):
    role = member.guild.get_role(1501020726495285350)
    channel = self.get_channel(1501019824472723506)

    if channel:
      await channel.send(
        f'🎉 Welcome {member.mention} to **{member.guild.name}**\n'
        f'We are already {member.guild.member_count} members.'
      )

    if role:
      await member.add_roles(role)
      print(f'A role was assigned to {member.name}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
