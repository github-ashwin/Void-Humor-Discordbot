import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

token = os.getenv('DISCORD_BOT_TOKEN')
if token:
    bot.run(token)
else:
    print("Error: DISCORD_BOT_TOKEN not found in environment variables")
