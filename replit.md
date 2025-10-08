# Discord Bot

## Overview
A Discord bot built with Python using the discord.py library.

## Recent Changes
- 2025-10-08: Initial project setup with discord.py
- User dismissed Replit Discord integration, using manual token setup instead

## Setup
The bot requires a `DISCORD_BOT_TOKEN` secret to run. The token should be obtained from the Discord Developer Portal.

## Commands
- `!hello` - Bot greets the user
- `!ping` - Shows bot latency

## Architecture
- `bot.py` - Main bot file with commands and event handlers
- Uses discord.py with command prefix `!`
- Message content intent enabled for reading messages
