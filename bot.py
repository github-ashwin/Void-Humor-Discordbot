import os
import random
import json
import discord
from discord.ext import commands

# --- Initialization and Setup ---

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents) 

# Load quotes globally
try:
    with open('quotes.json', 'r') as f:
        VOID_HUMOR_QUOTES = json.load(f)
    print(f"Loaded {len(VOID_HUMOR_QUOTES)} quotes.")
except Exception as e:
    print(f"ERROR loading quotes: {e}")
    VOID_HUMOR_QUOTES = []


# --- Bot Events ---

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}. Ready to whisper absurdities.")
    # Sync global slash commands.
    try:
        await bot.tree.sync()
        print("Slash commands sync initiated.")
    except Exception as e:
        print(f"Sync failed: {e}")


# --- Slash Command ---

@bot.tree.command(name="voidhumor", description="Get a random, absurd, dark humor quote.")
async def voidhumor(interaction: discord.Interaction):
    """Retrieves and sends a random quote."""

    if VOID_HUMOR_QUOTES:
        quote = random.choice(VOID_HUMOR_QUOTES)
        message = f"**The Void Whispers:**\n>>> {quote}"
    else:
        message = "The void is silent. I couldn't find the quotes."

    await interaction.response.send_message(message)


# --- Run Bot ---

# Retrieve the token set in Replit Secrets
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN') 

if BOT_TOKEN:
    bot.run(BOT_TOKEN)
else:
    print('FATAL ERROR: DISCORD_BOT_TOKEN not found.')