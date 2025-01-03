import discord
from discord.ext import commands

class TopGG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("TopGG cog is ready")

def setup(bot):
    bot.add_cog(TopGG(bot))
