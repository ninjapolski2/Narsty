import discord
from discord.ext import commands

class statusUpdate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'n!help | {len(self.client.guilds)} serwerów.'))

    @commands.Cog.listener()
    async def on_guild_remove(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'n!help | {len(self.client.guilds)} serwerów.'))

def setup(client):
    client.add_cog(statusUpdate(client))