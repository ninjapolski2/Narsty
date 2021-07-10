import discord
import json
import asyncpg
import logging

from discord.ext import commands
from discord.ext.commands import CommandInvokeError

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logi.txt', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents1 = discord.Intents.all()

with open("configManager.json", 'r') as f:
    json_data = json.load(f)
    global prefix, extensions, guild_token
    global login, psswd, db, host_ip
    prefix, extensions, guild_token = json_data["prefix"], json_data["extensions"], json_data["token"]
    login, psswd, db, host_ip = json_data["user"], json_data["password"], json_data["database"], json_data["host"]

client = commands.Bot(command_prefix=prefix, intents=intents1)
client.remove_command('help')

async def create_db_pool():
    client.conn = await asyncpg.create_pool(user=login, password=psswd, database=db, host=host_ip, port='5432')

@client.event
async def on_ready():
    print("Dołączyłem.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='06.06.2021r. Twórca bota: @NinjaaaSK#7850'))

@client.command()
async def konfiguruj(ctx):
    if ctx.message.author.id == ctx.guild.owner_id:
        await ctx.guild.create_text_channel('🔔ninjaaamarket')
    else:
        await ctx.send("Nie masz dostępu do tej komendy! Tylko własciciel serwera ma uprawnienia.")

@client.event
async def on_guild_join(guild):
    channel = discord.utils.find(lambda r: r.name == '🔔ninjaaamarket', guild.text_channels)
    if channel in guild:
        pass
    else:
        await guild.create_text_channel('🔔ninjaaamarket')

@client.command()
async def load(ctx, extension):
    if ctx.message.author.id == 318824628439089152:
        try:
            client.load_extension(extension)
            print(f'Załadowano {extension}')
        except Exception as error:
            print(f'{extension} nie może się załadować. [{error}]')
    else:
        embed = discord.Embed(title="NinjaaaMarket", description="Nie masz dostępu do tej komendy!", color=discord.Color.dark_red())
        await ctx.send(embed=embed)

@client.command()
async def unload(ctx, extension):
    if ctx.message.author.id == 318824628439089152:
        try:
            client.unload_extension(extension)
            print(f'Rozłączono {extension}')
        except Exception as error:
            print(f'{extension} nie może się odłączyć. [{error}]')
    else:
        embed = discord.Embed(title="NinjaaaMarket", description="Nie masz dostępu do tej komendy!", color=discord.Color.dark_red())
        await ctx.send(embed=embed)

@client.listen()
async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return

    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="NinjaaaMarket", description=f"{ctx.author.mention}, taka komenda nie istnieje.", color=discord.Color.orange())
        await ctx.send(embed=embed)
    elif isinstance(error, CommandInvokeError):
        embed = discord.Embed(title="NinjaaaMarket", description=f"{ctx.author.mention}, masz już utworzoną ofertę na (może innym) serwerze.", color=discord.Color.orange())
        await ctx.send(embed=embed)
    elif isinstance(error, asyncpg.UniqueViolationError):
        embed = discord.Embed(title="NinjaaaMarket", description=f"{ctx.author.mention}, masz już utworzoną ofertę na (może innym) serwerze.", fcolor=discord.Color.orange())
        await ctx.send(embed=embed)
    else:
        raise error

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Nie udało się załadować rozszerzenia {extension}\n{exc}')

client.loop.run_until_complete(create_db_pool())
client.run(guild_token)