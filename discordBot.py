# Class Libraries
import discord 
import os 
import random 
from ec2_metadata import ec2_metadata 

# Output to make sure the class libraris works.
print(ec2_metadata.region)
print(ec2_metadata.instance_id)

# Create the client object and the secret token key.
client = discord.Bot() 
token = str(os.getenv('TOKEN'))

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

	if channel == "playground": 
		if user_message.lower() == "hello" or user_message.lower() == "hi": 
			await message.channel.send(f'Hello {username}') 
			return
		elif user_message.lower() == "weather": 
			await message.channel.send(f'Raining as usual {username}') 

client.run(token)
		
