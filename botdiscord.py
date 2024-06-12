#Importing class libraries
import discord
import os
import random
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

#Print ec2 instance region and instance ID
print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#Get bot token from environment and set up discord intents for bot events
token = str(os.getenv('TOKEN')) #
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

#Creating a discord client instance
client = discord.Client(intents=intents)

#Prints text when the bot has been connected
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

#Retrieves information from message, like the content, the username and channel
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    #Prints information retrieved
    print(f'Message {user_message} by {username} on {channel}')

    #Ignores the messages that were sent by the bot
    if message.author == client.user:
        return
    
    #If the following message was sent in the aws channel, send the following message
    if channel == 'aws':
        if user_message.lower() == "marco?":
            await message.channel.send(f"Polo! Hello, {username}. Your EC2 Data: {ec2_metadata.region}")
            return
        
        #Respond to the specific text with the following text
        elif user_message.lower() == "work it, make it, do it, makes us":
            await message.channel.send(f'Harder, better, faster, stronger')
        
        #Respond to the following text with the sender's username and ec2 region
        elif user_message.lower() == "give me my ec2 data":
            await message.channel.send("{username}, your instance data is" + ec2_metadata.region)

#Run the bot with the token from before
client.run(token)
