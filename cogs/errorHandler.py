import discord
from discord.ext import commands

class errorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        error = getattr(error, "original", error)
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, taka komenda nie istnieje.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            raise error

def setup(client):
    client.add_cog(errorHandler(client))