import discord
from dotenv import load_dotenv
import os
import constants

load_dotenv(".env")

client = discord.Client(intents=constants.intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.content == "$hello":
        await message.channel.send("HELLO!")

client.run(os.getenv("TOKEN"))