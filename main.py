import os
import discord  


client = discord.Client()

@client.event
async def on_ready():
 print("we have logged in as {0.user}".format(client))
@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f"{username}: {user_message}({channel})")
  if message.content.startswith("!hello"):
    await message.channel.send(f"Hello Nigger {message.author}")
    
my_secret = os.environ['TOKEN']
client.run(my_secret)
