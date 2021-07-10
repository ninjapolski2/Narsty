import discord
import datetime
import asyncpg
from datetime import timezone, datetime
from discord.ext import commands
from discord.ext.commands import CommandInvokeError


class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def admin_usun_oferte(self, ctx, guildid: int):
        query1 = 'SELECT "creator_id" FROM creator'
        result1 = await self.client.conn.fetchval(query1)
        if ctx.message.author.id == result1:
            query2 = 'SELECT "guild_id" FROM adversitements WHERE "guild_id" = $1'
            result2 = await self.client.conn.fetchval(query2, guildid)
            if result2:
                queryDel1 = 'DELETE FROM adversitements WHERE "guild_id" = $1'
                queryDel2 = 'DELETE FROM owners WHERE "guild_id" = $1'
                await self.client.conn.execute(queryDel1, guildid)
                await self.client.conn.execute(queryDel2, guildid)
                query3 = 'SELECT "guild_id" FROM adversitements WHERE "guild_id" = $1'
                result3 = await self.client.conn.fetchval(query3, guildid)
                if not result3:
                    embed = discord.Embed(title='Narsty', description='Usunięto ofertę.', color=discord.Color.orange())
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Nie udało się usunąć oferty, spróbuj ponownie.")
            else:
                await ctx.send(f"Serwer nie ma utworzonej oferty.")
        else:
            embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś twórcą bota).', color=discord.Color.orange())
            await ctx.send(embed=embed)

    @admin_usun_oferte.error
    async def admin_usun_oferte_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj dane do tej komendy.", color = discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color = discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.DataError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            raise error

    @commands.command()
    async def admin_daj_premium(self, ctx, ownerid: int, *, args):
        query1 = 'SELECT "creator_id" FROM creator'
        result1 = await self.client.conn.fetchval(query1)
        if ctx.message.author.id == result1:
            query2 = 'SELECT "owner_id" FROM premium_people WHERE "owner_id" = $1'
            result2 = await self.client.conn.fetchval(query2, ownerid)
            if not result2:
                queryAdd1 = 'INSERT INTO premium_people ("owner_id", "date") VALUES ($1, $2)'
                dateTime = datetime.now(timezone.utc)
                await self.client.conn.execute(queryAdd1, ownerid, dateTime)
                embed = discord.Embed(title='Narsty', description='Nadano poprawnie użytkownikowi dostęp premium.', color=discord.Color.orange())
                await ctx.send(embed=embed)
                user = self.client.get_user(ownerid)
                embed = discord.Embed(title='Narsty', description=f'Dostałeś dostęp premium do bota Narsty \n Powód: {args}.', color=discord.Color.orange())
                await user.send(embed=embed)
            else:
                embed = discord.Embed(title='Narsty', description='Użytkownik ma już dostęp premium lub podano niepoprawne dane.', color=discord.Color.orange())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś twórcą bota).', color=discord.Color.orange())
            await ctx.send(embed=embed)

    @admin_daj_premium.error
    async def admin_daj_premium_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, CommandInvokeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, ID tego użytkownika jest już bazie danych.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.UniqueViolationError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, ID tego użytkownika jest już bazie danych.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, AttributeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, Nie możesz podać ID bota lub nieistniejącego konta.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.DataError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            raise error

    @commands.command()
    async def admin_zabierz_premium(self, ctx, ownerid: int, *, args):
        query1 = 'SELECT "creator_id" FROM creator'
        result1 = await self.client.conn.fetchval(query1)
        if ctx.message.author.id == result1:
            query2 = 'SELECT "owner_id" FROM premium_people WHERE "owner_id" = $1'
            result2 = await self.client.conn.fetchval(query2, ownerid)
            if result2:
                queryDel1 = 'DELETE FROM premium_people WHERE "owner_id" = $1'
                await self.client.conn.execute(queryDel1, ownerid)
                embed = discord.Embed(title='Narsty', description='Zabrano użytkownikowi dostęp premium.', color=discord.Color.orange())
                await ctx.send(embed=embed)
                user = self.client.get_user(ownerid)
                embed = discord.Embed(title='Narsty', description=f'Zabrano tobie dostęp premium do bota Narsty \n Powód: {args}.', color=discord.Color.orange())
                await user.send(embed=embed)
            else:
                embed = discord.Embed(title='Narsty', description='Nie ma tego ID użytkownika w bazie danych.', color=discord.Color.orange())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś twórcą bota).', color=discord.Color.orange())
            await ctx.send(embed=embed)

    @admin_zabierz_premium.error
    async def admin_zabierz_premium_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.DataError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, AttributeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, Nie możesz podać ID bota lub nieistniejącego konta.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            raise error

    @commands.command()
    async def admin_nadaj_blackliste(self, ctx, ownerid: int, guildid: int, *, args):
            query1 = 'SELECT "creator_id" FROM creator'
            result1 = await self.client.conn.fetchval(query1)
            if ctx.message.author.id == result1:
                query2 = 'SELECT "owner_id" FROM blacklist WHERE "guild_id" = $1'
                result2 = await self.client.conn.fetchval(query2, guildid)
                if not result2:
                    dateTime = datetime.now(timezone.utc)
                    queryAdd1 = 'INSERT INTO blacklist ("owner_id", "guild_id", "date") VALUES ($1, $2, $3)'
                    await self.client.conn.execute(queryAdd1, ownerid, guildid, dateTime)
                    embed = discord.Embed(title='Narsty', description='Wpisano użytkownika do blacklisty.', color=discord.Color.orange())
                    await ctx.send(embed=embed)
                    user = self.client.get_user(ownerid)
                    embed = discord.Embed(title='Narsty', description=f'Wpisano cię do blacklisty. \n Powód: {args}', color=discord.Color.orange())
                    await user.send(embed=embed)
                else:
                    embed = discord.Embed(title='Narsty', description='Sprawdź, czy na pewno podałeś prawidłowe ID użytkownika oraz ID serwera.', color=discord.Color.orange())
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś twórcą bota).', color=discord.Color.orange())
                await ctx.send(embed=embed)


    @admin_nadaj_blackliste.error
    async def admin_nadaj_blackliste_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, CommandInvokeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, ID tego gracza jest już w bazie danych.", color = discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.UniqueViolationError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, ID tego gracza jest już w bazie danych.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.DataError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, AttributeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, Nie możesz podać ID bota lub nieistniejącego konta.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            raise error

    @commands.command()
    async def admin_zabierz_blackliste(self, ctx, ownerid: int, guildid: int, *, args):
        query1 = 'SELECT "creator_id" FROM creator'
        result1 = await self.client.conn.fetchval(query1)
        if ctx.message.author.id == result1:
            query2 = 'SELECT "owner_id" FROM blacklist WHERE "guild_id" = $1'
            result2 = await self.client.conn.fetchval(query2, guildid)
            if result2:
                queryDel1 = 'DELETE FROM blacklist WHERE "guild_id" = $1'
                await self.client.conn.execute(queryDel1, guildid)
                embed = discord.Embed(title='Narsty', description='Wypisano użytkownika z blacklisty.', color=discord.Color.orange())
                await ctx.send(embed=embed)
                user = self.client.get_user(ownerid)
                embed = discord.Embed(title='Narsty', description=f'Wypisano cię z blacklisty. \n Powód: {args}.', color=discord.Color.orange())
                await user.send(embed=embed)
            else:
                embed = discord.Embed(title='Narsty', description='Sprawdź, czy na pewno podałeś prawidłowe ID użytkownika oraz ID serwera.', color=discord.Color.orange())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś twórcą bota).', color=discord.Color.orange())
            await ctx.send(embed=embed)

    @admin_zabierz_blackliste.error
    async def admin_zabierz_blackliste_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.DataError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, AttributeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, Nie możesz podać ID bota lub nieistniejącego konta.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            raise error

    @commands.command()
    async def admin_zresetuj_kolejke(self, ctx):
        query1 = 'SELECT "creator_id" FROM creator'
        result1 = await self.client.conn.fetchval(query1)
        if ctx.message.author.id == result1:
            queryUpdate1 = 'UPDATE adv_queue SET "queue_number" = 1'
            await self.client.conn.execute(queryUpdate1)
            query2 = 'SELECT "queue_number" FROM adv_queue WHERE "queue_number" = 1'
            result2 = await self.client.conn.fetchval(query2)
            embed = discord.Embed(title='Narsty', description=f'Sukces! Miejsce: {result2}', color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś twórcą bota).', color=discord.Color.orange())
            await ctx.send(embed=embed)


    @commands.command()
    async def admin_pokaz_oferte(self, ctx, guildid: int):
        query1 = 'SELECT "creator_id" FROM creator'
        result1 = await self.client.conn.fetchval(query1)
        if ctx.message.author.id == result1:
            query2 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
            query3 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
            result2 = await self.client.conn.fetchval(query2, guildid)
            result3 = await self.client.conn.fetchval(query3, guildid)
            if result2:
                embed = discord.Embed(title='Narsty', description=f' ID serwera: {guildid} \n ID właściciela: {result2} \n\n {result3} ', color=discord.Color.orange())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title='Narsty', description='Ten serwer nie posiada swojej oferty.', color=discord.Color.orange())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś twórcą bota).', color=discord.Color.orange())
            await ctx.send(embed=embed)

    @admin_pokaz_oferte.error
    async def admin_pokaz_oferte_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.DataError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            raise error

def setup(client):
    client.add_cog(admin(client))