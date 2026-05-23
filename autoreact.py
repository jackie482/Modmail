import discord
import os
import asyncio

# PUT YOUR USER ID HERE
# You are the target user. When you type, the bot will react.
TARGET_USER_ID = 1387497456740339824

# PUT THE CUSTOM EMOJI TEXT HERE
# Note: Keep the exact format inside the quotes, including the angle brackets and colon.
CUSTOM_EMOJI = "<:67:1507549169450221708>" 

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Auto-React script logged in as {client.user}")

@client.event
async def on_message(message):
    # Triggers only when YOU type in a server text channel
    if message.guild and message.author.id == TARGET_USER_ID:
        try:
            # We use the full custom emoji string here
            await message.add_reaction(CUSTOM_EMOJI)
        except Exception as e:
            # This is useful for debugging. If the reaction fails, you will see why in the logs.
            print(f"Failed to react: {e}")

# Uses the same bot token as your modmail bot
# The token is stored as an environment variable for security.
client.run(os.environ.get("TOKEN"))
