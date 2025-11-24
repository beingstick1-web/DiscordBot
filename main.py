import discord
from discord.ext import commands

TOKEN = "MTQ0MjQyMjQ1NDkxNTA0MzQxMQ.GAITDI.Z5H6Y_RjLnEGgHkY4Zmvred3ify84hTHoKoKaw"

DM_MESSAGE = """
🔥 Welcome to **CARNAGE**!

The CARNAGE SEEKS LOYALTY
THE WAR AWAITS YOU

If you need help, DM the staff anytime.
"""

intents = discord.Intents.default()
intents.members = True  # Needed for join detection

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_member_join(member):
    try:
        await member.send(DM_MESSAGE)
        print(f"Sent DM to {member.name}")
    except Exception as e:
        print(f"Could not DM {member.name}: {e}")

bot.run(TOKEN)
