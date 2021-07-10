import discord
import datetime
import asyncpg
from datetime import timezone, datetime
from discord.ext import commands

class general(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def usun_oferte(self, ctx):
        if ctx.message.author.id == ctx.guild.owner_id:
            memberCount = 0
            for member in ctx.guild.members:
                if member.bot:
                    pass
                elif member:
                    memberCount += 1
            if memberCount >= 1:
                guildID = ctx.guild.id
                query1 = 'SELECT "guild_id" FROM adversitements WHERE "guild_id" = $1'
                result1 = await self.client.conn.fetchval(query1, guildID)
                if result1:
                    guildID = ctx.guild.id
                    queryDel1 = 'DELETE FROM owners WHERE "guild_id" = $1'
                    await self.client.conn.execute(queryDel1, guildID)
                    queryDel2 = 'DELETE FROM adversitements WHERE "guild_id" = $1'
                    await self.client.conn.execute(queryDel2, guildID)
                    query2 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                    result2 = await self.client.conn.fetchval(query2, guildID)
                    if not result2:
                        embed = discord.Embed(title="Narsty", description="Usunięto ofertę.", color=discord.Color.orange())
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="Narsty", description="Nie usunięto oferty, spróbuj ponownie. Jeśli nie zadziała, napisz do supportu bota.", color=discord.Color.orange())
                        await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Narsty", description="Oferta nie jest utworzona dla tego serwera.", color=discord.Color.orange())
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Narsty", description="Ten serwer musi mieć co najmniej 1 osobę (nie boty).", color=discord.Color.orange())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Narsty", description="Nie masz dostępu do tej komendy (nie jesteś właścicielem serwera).", color=discord.Color.orange())
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dodaj_oferte(self, ctx, *, args):
            if ctx.message.author.id == ctx.guild.owner_id:
                guildID = ctx.guild.id
                query1 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                result1 = await self.client.conn.fetchval(query1, guildID)
                memberCount = 0
                for member in ctx.guild.members:
                    if member.bot:
                        pass
                    elif member:
                        memberCount += 1
                if memberCount >= 1:
                    if ctx.message.mention_everyone:
                        if "@everyone" in ctx.message.content or "@here" in ctx.message.content:
                            query2 = 'SELECT "owner_id" FROM premium_people WHERE "owner_id" = $1'
                            result2 = await self.client.conn.fetchval(query2, ctx.guild.owner_id)
                            if result2:
                                query3 = 'SELECT "owner_id" FROM blacklist WHERE "guild_id" = $1'
                                result3 = await self.client.conn.fetchval(query3, ctx.guild.id)
                                query4 = 'SELECT "owner_id" FROM owners WHERE "guild_id" = $1'
                                result4 = await self.client.conn.fetchval(query4, ctx.guild.id)
                                query5 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                                result5 = await self.client.conn.fetchval(query5, ctx.guild.id)
                                if result4 or result5:
                                    embed = discord.Embed(title='Narsty', description='Masz już utworzoną ofertę. Jeżeli nie, to skontaktuj się z supportem.', color=discord.Color.orange())
                                    await ctx.send(embed=embed)
                                elif result3:
                                    embed = discord.Embed(title='Narsty', description='Zostałeś zbanowany. Wszelkie wyjaśnienia, odwołania złóż do supportu.', color=discord.Color.orange())
                                    await ctx.send(embed=embed)
                                else:
                                    guildID = ctx.guild.id
                                    dateTime = datetime.now(timezone.utc)
                                    queryAdd1 = 'INSERT INTO owners ("guild_id", "owner_id", "date") VALUES ($1, $2, $3)'
                                    await self.client.conn.execute(queryAdd1, guildID, ctx.message.author.id, dateTime)
                                    queryAdd2 = 'INSERT INTO adversitements ("guild_id", "owner_id", "date", "adv_description") VALUES ($1, $2, $3, $4)'
                                    await self.client.conn.execute(queryAdd2, guildID, ctx.guild.owner_id, dateTime, args)
                                    query6 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                                    query7 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                                    result6 = await self.client.conn.fetchval(query6, guildID)
                                    result7 = await self.client.conn.fetchval(query7, guildID)
                                    embed = discord.Embed(title="Narsty", description="Sukces! Twoja reklama wygląda tak: ", color=discord.Color.orange())
                                    await ctx.send(embed=embed)
                                    embed = discord.Embed(title='Narsty', description=f"Reklama właściciela: {result6} \n \n {result7}", color=discord.Color.orange())
                                    await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title="Narsty", description="Nie masz uprawnień do użycia wzmianki everyone lub here (nie masz dostępu premium).", color=discord.Color.orange())
                                await ctx.send(embed=embed)
                        elif result1:
                            guildID = ctx.guild.id
                            query8 = 'SELECT "owner_id" FROM blacklist WHERE "guild_id" = $1'
                            result8 = await self.client.conn.fetchval(query8, guildID)
                            query9 = 'SELECT "owner_id" FROM owners WHERE "guild_id" = $1'
                            result9 = await self.client.conn.fetchval(query9, guildID)
                            query10 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                            result10 = await self.client.conn.fetchval(query10, guildID)
                            if result9 & result10:
                                embed = discord.Embed(title='Narsty', description='Masz już utworzoną ofertę. Jeżeli nie, to skontaktuj się z supportem.', color=discord.Color.orange())
                                await ctx.send(embed=embed)
                            elif result8:
                                embed = discord.Embed(title='Narsty', description='Zostałeś zbanowany. Wszelkie wyjaśnienia, odwołania złóż do supportu.', color=discord.Color.orange())
                                await ctx.send(embed=embed)
                            else:
                                guildID = ctx.guild.id
                                dateTime = datetime.now(timezone.utc)
                                queryAdd3 = 'INSERT INTO owners ("guild_id", "owner_id","date") VALUES ($1, $2, $3)'
                                await self.client.conn.execute(queryAdd3, guildID, ctx.message.author.id, dateTime)
                                queryAdd4 = 'INSERT INTO adversitements ("guild_id", "owner_id", "date", "adv_description") VALUES ($1, $2, $3, $4)'
                                await self.client.conn.execute(queryAdd4, guildID, ctx.guild.owner_id, dateTime, args)
                                query11 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                                query12 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                                result11 = await self.client.conn.fetchval(query11, guildID)
                                result12 = await self.client.conn.fetchval(query12, guildID)
                                embed = discord.Embed(title='Narsty', description=f"Sukces! Twoja reklama wygląda tak:  \n\n Reklama właściciela: {result11} \n \n {result12}", color=discord.Color.orange())
                                await ctx.send(embed=embed)
                        else:
                            embed = (discord.Embed(title="Narsty", description="Nie masz uprawnień do użycia wzmianki everyone lub here (nie masz dostępu premium).", color=discord.Color.orange()))
                            await ctx.send(embed=embed)

                    else:
                        guildID = ctx.guild.id
                        query13 = 'SELECT "owner_id" FROM blacklist WHERE "guild_id" = $1'
                        result13 = await self.client.conn.fetchval(query13, guildID)
                        query14 = 'SELECT "owner_id" FROM owners WHERE "guild_id" = $1'
                        result14 = await self.client.conn.fetchval(query14, guildID)
                        query15 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                        result15 = await self.client.conn.fetchval(query15, guildID)
                        if result14 or result15:
                            embed = discord.Embed(title='Narsty', description='Masz już utworzoną ofertę. Jeżeli nie, to skontaktuj się z supportem.', color=discord.Color.orange())
                            await ctx.send(embed=embed)
                        elif result13:
                            embed = discord.Embed(title='Narsty', description='Zostałeś zbanowany. Wszelkie wyjaśnienia, odwołania złóż do supportu.', color=discord.Color.orange())
                            await ctx.send(embed=embed)
                        else:
                            guildID = ctx.guild.id
                            dateTime = datetime.now(timezone.utc)
                            queryAdd5 = 'INSERT INTO owners ("guild_id", "owner_id", "date") VALUES ($1, $2, $3)'
                            await self.client.conn.execute(queryAdd5, guildID, ctx.message.author.id, dateTime)
                            queryAdd6 = 'INSERT INTO adversitements ("guild_id", "owner_id", "date", "adv_description") VALUES ($1, $2, $3, $4)'
                            await self.client.conn.execute(queryAdd6, guildID, ctx.guild.owner_id, dateTime, args)
                            query16 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                            query17 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                            result16 = await self.client.conn.fetchval(query16, guildID)
                            result17 = await self.client.conn.fetchval(query17, guildID)
                            embed = discord.Embed(title="Narsty", description="Sukces! Twoja reklama wygląda tak: ", color=discord.Color.orange())
                            await ctx.send(embed=embed)
                            embed = discord.Embed(title='Narsty', description=f"Reklama właściciela: {result16} \n \n {result17}", color=discord.Color.orange())
                            await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Narsty", description="Ten serwer musi mieć co najmniej 1 osobę (nie boty).", color=discord.Color.orange())
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Narsty", description="Nie masz uprawnień do użycia tej komendy!", color=discord.Color.orange())
                await ctx.send(embed=embed)

    @dodaj_oferte.error
    async def dodaj_oferte_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.message.author.mention}, podaj dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, masz już utworzoną ofertę na innym serwerze. [1]", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.UniqueViolationError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, masz już utworzoną ofertę na innym serwerze. [2]", color=discord.Color.orange())
            await ctx.send(embed=embed)
        elif isinstance(error, asyncpg.DataError):
            embed = discord.Embed(title="Narsty", description=f"{ctx.author.mention}, podaj prawidłowe dane do tej komendy.", color=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            raise error

    @commands.command()
    async def zaaktualizuj_oferte(self, ctx, *, args):
        if ctx.message.author.id == ctx.guild.owner_id:
            memberCount = 0
            for member in ctx.guild.members:
                if member.bot:
                    pass
                elif member:
                    memberCount += 1
            if memberCount >= 1:
                if ctx.message.mention_everyone:
                    if "@everyone" in ctx.message.content or "@here" in ctx.message.content:
                        query18 = 'SELECT "owner_id" FROM premium_people WHERE "owner_id" = $1'
                        result18 = await self.client.conn.fetchval(query18, ctx.guild.owner_id)
                        if not result18:
                            embed = discord.Embed(title="Narsty", description="Nie masz uprawnień do użycia wzmianki everyone lub here (nie masz dostępu premium).", color=discord.Color.orange())
                            await ctx.send(embed=embed)

                        else:
                            guildID = ctx.guild.id
                            query19 = 'SELECT "owner_id" FROM blacklist WHERE "guild_id" = $1'
                            result19 = await self.client.conn.fetchval(query19, guildID)
                            query20 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                            result20 = await self.client.conn.fetchval(query20, guildID)
                            query21 = 'SELECT "owner_id" FROM owners WHERE "guild_id" = $1'
                            result21 = await self.client.conn.fetchval(query21, guildID)
                            if result19:
                                embed = discord.Embed(title='Narsty', description='Zostałeś zbanowany. Wszelkie wyjaśnienia, odwołania złóż do supportu.', color=discord.Color.orange())
                                await ctx.send(embed=embed)
                            elif not result20 or not result21:
                                embed = discord.Embed(title="Narsty", description="Oferta nie jest utworzona dla tego serwera.", color=discord.Color.orange())
                                await ctx.send(embed=embed)
                            else:
                                guildID = ctx.guild.id
                                dateTime = datetime.now(timezone.utc)
                                queryUpdate1 = 'UPDATE owners SET "owner_id" = $1 WHERE "guild_id" = $2'
                                queryUpdate2 = 'UPDATE owners SET "date" = $1 WHERE "guild_id" = $2'
                                queryUpdate3 = 'UPDATE adversitements SET "owner_id" = $1 WHERE "guild_id" = $2'
                                queryUpdate4 = 'UPDATE adversitements SET "date" = $1 WHERE "guild_id" = $2'
                                queryUpdate5 = 'UPDATE adversitements SET "adv_description" = $1 WHERE "guild_id" = $2'
                                query22 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                                if query22:
                                    await self.client.conn.execute(queryUpdate1, ctx.guild.owner_id, guildID)
                                    await self.client.conn.execute(queryUpdate2, dateTime, guildID)
                                    await self.client.conn.execute(queryUpdate4, dateTime, guildID)
                                    await self.client.conn.execute(queryUpdate3, ctx.guild.owner_id, guildID)
                                    await self.client.conn.execute(queryUpdate5, args, guildID)
                                    query22 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                                    query23 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                                    result22 = await self.client.conn.fetchval(query22, guildID)
                                    result23 = await self.client.conn.fetchval(query23, guildID)
                                    embed = discord.Embed(title="Narsty", description=f"Sukces! Twoja reklama wygląda tak: \n\n Reklama właściciela: {result22} \n \n {result23}", color=discord.Color.orange())
                                    await ctx.send(embed=embed)
                                else:
                                    embed = discord.Embed(title='Narsty', description='Masz już utworzoną ofertę. Jeżeli nie, to skontaktuj się z supportem.', color=discord.Color.orange())
                                    await ctx.send(embed=embed)
                    else:
                        query24 = 'SELECT "guild_id" FROM adversitements WHERE "guild_id" = $1'
                        result24 = await self.client.conn.fetchval(query24, ctx.guild.id)
                        if result24:
                            guildID = ctx.guild.id
                            dateTime = datetime.now(timezone.utc)
                            queryUpdate6 = 'UPDATE owners SET "owner_id" = $1 WHERE "guild_id" = $2'
                            queryUpdate7 = 'UPDATE owners SET "date" = $1 WHERE "guild_id" = $2'
                            queryUpdate8 = 'UPDATE adversitements SET "owner_id" = $1 WHERE "guild_id" = $2'
                            queryUpdate9 = 'UPDATE adversitements SET "adv_description" = $1 WHERE "guild_id" = $2'
                            queryUpdate10 = 'UPDATE adversitements SET "date" = $1 WHERE "guild_id" = $2'
                            query25 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                            query26 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                            result25 = await self.client.conn.fetchval(query25, guildID)
                            result26 = await self.client.conn.fetchval(query26, guildID)
                            if result25:
                                await self.client.conn.execute(queryUpdate6, guildID, ctx.guild.owner_id)
                                await self.client.conn.execute(queryUpdate8, ctx.guild.owner_id, guildID)
                                await self.client.conn.execute(queryUpdate9, args, guildID)
                                await self.client.conn.execute(queryUpdate7, dateTime, guildID)
                                await self.client.conn.execute(queryUpdate10, dateTime, guildID)
                                embed = discord.Embed(title="Narsty", description=f"Sukces! Twoja reklama wygląda tak: \n\n Reklama właściciela: {result25} \n \n {result26}", color=discord.Color.orange())
                                await ctx.send(embed=embed)
                            else:
                                embed = discord.Embed(title='Narsty', description='Masz już utworzoną ofertę. Jeżeli nie, to skontaktuj się z supportem.', color=discord.Color.orange())
                                await ctx.send(embed=embed)
                else:
                    guildID = ctx.guild.id
                    query27 = 'SELECT "owner_id" FROM blacklist WHERE "guild_id" = $1'
                    result27 = await self.client.conn.fetchval(query27, guildID)
                    query28 = 'SELECT "owner_id" FROM owners WHERE "guild_id" = $1'
                    result28 = await self.client.conn.fetchval(query28, guildID)
                    query29 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                    result29 = await self.client.conn.fetchval(query29, guildID)
                    if not result28 or not result29:
                        embed = discord.Embed(title="Narsty", description="Oferta nie jest utworzona dla tego serwera.", color=discord.Color.orange())
                        await ctx.send(embed=embed)
                    elif result27:
                        embed = discord.Embed(title='Narsty', description='Zostałeś zbanowany. Wszelkie wyjaśnienia, odwołania złóż do supportu.', color=discord.Color.orange())
                        await ctx.send(embed=embed)
                    else:
                        guildID = ctx.guild.id
                        dateTime = datetime.now(timezone.utc)
                        queryUpdate11 = 'UPDATE owners SET "owner_id" = $1 WHERE "guild_id" = $2'
                        queryUpdate12 = 'UPDATE adversitements SET "owner_id" = $1 WHERE "guild_id" = $2'
                        queryUpdate13 = 'UPDATE adversitements SET "adv_description" = $1 WHERE "guild_id" = $2'
                        queryUpdate14 = 'UPDATE adversitements SET "date" = $1 WHERE "guild_id" = $2'
                        query30 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                        query31 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                        await self.client.conn.execute(queryUpdate11, ctx.guild.owner_id, guildID)
                        await self.client.conn.execute(queryUpdate12, ctx.guild.owner_id, guildID)
                        await self.client.conn.execute(queryUpdate14, dateTime, guildID)
                        await self.client.conn.execute(queryUpdate13, args, guildID)
                        result30 = await self.client.conn.fetchval(query30, guildID)
                        result31 = await self.client.conn.fetchval(query31, guildID)
                        embed = discord.Embed(title="Narsty", description="Sukces! Twoja reklama wygląda tak: ", color=discord.Color.orange())
                        await ctx.send(embed=embed)
                        embed = discord.Embed(title='Narsty', description=f"\n\n Reklama właściciela: {result30} \n \n {result31}", color=discord.Color.orange())
                        await ctx.send(embed=embed)
            else:
                await ctx.send("Ten serwer musi mieć co najmniej 1 osobę (nie boty).")
        else:
            embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś właścicielem serwera).', color=discord.Color.orange())
            await ctx.send(embed=embed)

    @zaaktualizuj_oferte.error
    async def zaaktualizuj_oferte_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Narsty", description=f"{ctx.message.author.mention}, podaj dane do tej komendy.", color=discord.Color.orange())
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
    async def kolejkacheck(self, ctx):
        memberCount = 0
        for member in ctx.guild.members:
            if member.bot:
                pass
            elif member:
                memberCount += 1
        if memberCount >= 1:
            query32 = 'SELECT "queue_number" FROM adv_queue'
            result32 = await self.client.conn.fetchval(query32)
            if not result32:
                embed = discord.Embed(title="Narsty", description="Aktualnie kolejka jest wyłączona.", color=discord.Color.orange())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Narsty", description="Teraz zostanie wyświetlona reklama pod nr w kolejce: {result32+1}", color=discord.Color.orange())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Narsty", description="Ten serwer musi mieć co najmniej 1 osobę (nie boty).", color=discord.Color.orange())
            await ctx.send(embed=embed)

    @commands.command()
    async def pokaz_oferte(self, ctx):
        if ctx.message.author.id == ctx.guild.owner_id:
            memberCount = 0
            for member in ctx.guild.members:
                if member.bot:
                    pass
                elif member:
                    memberCount += 1
            if memberCount >= 1:
                query33 = 'SELECT "owner_id" FROM adversitements WHERE "guild_id" = $1'
                query34 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                result33 = await self.client.conn.fetchval(query33, ctx.guild.id)
                result34 = await self.client.conn.fetchval(query34, ctx.guild.id)
                if result34:
                    embed = discord.Embed(title="Narsty", description=f"Reklama właściciela: {result33} \n \n {result34}", color=discord.Color.orange())
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Narsty", description="Oferta nie jest utworzona dla tego serwera.", color=discord.Color.orange())
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Narsty", description="Ten serwer musi mieć co najmniej 1 osobę (nie boty).", color=discord.Color.orange())
                await ctx.send(embed=embed)
        else:
                embed = discord.Embed(title='Narsty', description='Nie masz dostępu do tej komendy (nie jesteś właścicielem serwera).', color=discord.Color.orange())
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(general(client))
