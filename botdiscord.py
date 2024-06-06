#
import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

#
print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#
token = str(os.getenv('TOKEN')) #
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return
    
    if channel == 'aws':
        if user_message.lower() == "marco?":
            await message.channel.send(f"Polo! Hello, {username}.")
            return
        
        elif user_message.lower() == "work it, make it, do it, makes us":
            await message.channel.send(f'Harder, better, faster, stronger')
        
        elif user_message.lower() == "give me my ec2 data":
            await message.channel.send(f"{username}, your instance data is  {ec2_metadata.instance_id} Your EC2 Data: {ec2_metadata.region}")

client.run(token)
