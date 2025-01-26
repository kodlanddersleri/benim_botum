import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')


bot.run("MTMzMDU5Njk0NjgxMjg2NjYzMw.GaqcjJ.NVWEKR1ikHjE1YgBSbF8MLb6Np3eAK7oIQESGo")