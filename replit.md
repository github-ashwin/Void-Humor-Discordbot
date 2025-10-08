# Discord Bot: VoidHumor

## Overview
A Discord bot built with Python using the `discord.py` library. This bot provides **absurd, hilarious, dark humor quotes** sourced from a local JSON file.

---

## Recent Changes
- 2025-10-08: Initial project setup with `discord.py`.
- **2025-10-08: Migrated from prefix commands (`!`) to modern Slash Commands (`/`).**
- **2025-10-08: Implemented quote loading from `quotes.json`.**

---

## Setup
The bot requires the following in Replit's **Secrets** manager (the lock icon) to run:

| Secret Key | Value |
| :--- | :--- |
| **`DISCORD_BOT_TOKEN`** | The token obtained from the Discord Developer Portal. |

Ensure the **Message Content Intent** is enabled in the Discord Developer Portal.

---

## Commands
The bot uses **Slash Commands** (commands starting with `/`) which are automatically registered upon startup.

- **`/voidhumor`** - Retrieves a random, absurd, dark humor quote from the internal quote database.

*(Note: The old `!hello` and `!ping` prefix commands were removed in favor of the new slash command structure.)*

---

## Architecture
- **`bot.py`**: Main bot logic, event handlers, and the implementation for the `/voidhumor` slash command.
- **`quotes.json`**: An external **JSON Array** containing all the dark humor quotes. The bot loads this file on startup.
- Uses `discord.py` and the application command tree for modern Discord interaction.
- Message content intent is enabled, although only required for future prefix commands or message scanning.