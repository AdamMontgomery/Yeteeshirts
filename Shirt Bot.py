import discord
from scrape import getshirturls
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!shirts'):
        await message.channel.send('\n'.join(getshirturls()))


client.run('MTEzMjcxMTQ5ODQ3Nzc0ODI5NA.G0gY2H.f5cVhRD-EPxV9WIXZbMYwIvkUBL907898ZwTLM')