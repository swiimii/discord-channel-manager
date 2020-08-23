from tokenInformation import DiscordAPIToken

import discord

TOKEN = DiscordAPIToken

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(DiscordAPIToken)
