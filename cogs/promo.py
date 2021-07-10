import random
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class promo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.cooldown(2, 86400, BucketType.user)
    @commands.command()
    async def promuj_oferte(self, ctx):
        if ctx.message.author.id == ctx.guild.owner_id:
            query1 = 'SELECT "owner_id" FROM blacklist WHERE "guild_id" = $1'
            result1 = await self.client.conn.fetchval(query1, ctx.guild.id)
            if result1:
                embed = discord.Embed(title='Narsty', description='Zostałeś zbanowany. Wszelkie wyjaśnienia, odwołania złóż do supportu.', color=discord.Color.orange())
                await ctx.send(embed=embed)
            else:
                query2 = 'SELECT "owner_id" FROM premium_people WHERE "owner_id" = $1'
                result2 = await self.client.conn.fetchval(query2, ctx.message.author.id)
                if result2:
                    serverListWyslaneOsoby = []
                    serverList = []
                    if len(self.client.guilds) > 10:
                        for i in range(11):
                            while True:
                                botGuilds = self.client.guilds
                                randomGuild = random.choice(botGuilds.name)
                                if str(randomGuild) in serverList:
                                    serverList.append(randomGuild)
                                    break
                            query3 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                            result3 = await self.client.conn.fetchval(query3, ctx.guild.id)
                            getRandomGuild = self.client.get_guild(randomGuild.id)
                            channel = discord.utils.find(lambda r: r.name == '🔔ninjaportal', getRandomGuild.text_channels)
                            if channel is not None:

                                try:
                                    await channel.send("Siema, zapewne nie raz chciałeś jakoś zarobić, mając umiejętności, ale nie wiesz jak się zareklamować lub wypromować?💰💰💰 \n Nasz bot ***NinjaManager*** oferuje reklamowanie Ciebie w zakresie: \n▫ kupię 💵 \n ▫ sprzedam 💵 \n ▫ wymienię się 💵 \n ▫ robię/zrobię 💵 \n ▫ potrzebuję 💵 \n ▫ szukam (kogoś, czegoś) 💵 \n Co trzeba spełnić, żeby twoja oferta znalazła się w kolejce: \n ▫ dodać naszego bota reklamującego oferty na serwerze \n ▫ stworzyć kanał :kiwi:ninjamanager z uprawnieniami wysyłania wiadomości tylko przez bota oraz możliwość wysyłania wzmianek everyone i here \n ▫ zapoznaj się z komendami za pomocą komendy n!help \n ▫ zapoznaj się z regulaminem, aby nie dostać blacklisty na twój serwer i twoje konto! Jak bot działa? \n ▪ Zostajesz zapisany do kolejki, gdzie reklamy są wysyłane co jakiś czas. Każda reklama ma jakiś numer. Bot wysyła po kolei reklamy co parę minut, aż dojdzie do końca. Jeśli ostatnia reklama w kolejce zostanie wysłana, bot znowu zaczyna wysyłać reklamy od początku listy. \n  https://discord.gg/s3J3TwpJh8")
                                    await channel.send(f"""\n \n **REKLAMA PROMOWANA** \n użytkownika: {str(ctx.message.author.name)} / {str(ctx.message.author.id)} \n\n {str(result3)} """)
                                    print(f"{i} -promowanie oferty serwera {ctx.guild.id} przez {ctx.author.id}")
                                    serverListWyslaneOsoby.append(getRandomGuild.name)
                                except discord.Forbidden:
                                    user = self.client.get_user(318824628439089152)
                                    await user.send(f"Usuń ofertę gildii {getRandomGuild.id}, powód: 'Bot nie może wysłać wiadomości na kanale tekstowym'")
                                    print(f"{i} -promowanie oferty serwera {ctx.guild.id} przez {ctx.author.id}")
                            else:
                                queryDel1 = 'DELETE FROM adversitements WHERE "owner_id" = $1'
                                randomGuild = random.choice(self.client.guilds)
                                getRandomGuild = self.client.get_guild(randomGuild.id)
                                user = self.client.get_user(getRandomGuild.owner_id)
                                try:
                                    embed = discord.Embed(title='Narsty', description='Usunąłem twoją ofertę, ponieważ nie posiadasz kanału do ofert.', color=discord.Color.orange())
                                    await user.send(embed=embed)
                                    await self.client.conn.execute(queryDel1, getRandomGuild.owner_id)
                                except discord.Forbidden:
                                    user = self.client.get_user(318824628439089152)
                                    await user.send(f"Usuń ofertę gildii {getRandomGuild.id}, gdzie właścicielem jest {user.name} / {user.id} powód: 'Bot nie może wysłać wiadomości do właściciela serwera {getRandomGuild}'")
                    else:
                        for i in range(11):
                            botGuilds = self.client.guilds
                            randomGuild = random.choice(botGuilds)
                            query3 = 'SELECT "adv_description" FROM adversitements WHERE "guild_id" = $1'
                            result3 = await self.client.conn.fetchval(query3, ctx.guild.id)
                            getRandomGuild = self.client.get_guild(randomGuild.id)
                            channel = discord.utils.find(lambda r: r.name == '🥝ninjamanager', getRandomGuild.text_channels)
                            if channel is not None:
                                try:
                                    await channel.send("Siema, zapewne nie raz chciałeś jakoś zarobić, mając umiejętności, ale nie wiesz jak się zareklamować lub wypromować?💰💰💰 \n Nasz bot ***NinjaManager*** oferuje reklamowanie Ciebie w zakresie: \n▫ kupię 💵 \n ▫ sprzedam 💵 \n ▫ wymienię się 💵 \n ▫ robię/zrobię 💵 \n ▫ potrzebuję 💵 \n ▫ szukam (kogoś, czegoś) 💵 \n Co trzeba spełnić, żeby twoja oferta znalazła się w kolejce: \n ▫ dodać naszego bota reklamującego oferty na serwerze \n ▫ stworzyć kanał :kiwi:ninjamanager z uprawnieniami wysyłania wiadomości tylko przez bota oraz możliwość wysyłania wzmianek everyone i here \n ▫ zapoznaj się z komendami za pomocą komendy n!help \n ▫ zapoznaj się z regulaminem, aby nie dostać blacklisty na twój serwer i twoje konto! Jak bot działa? \n ▪ Zostajesz zapisany do kolejki, gdzie reklamy są wysyłane co jakiś czas. Każda reklama ma jakiś numer. Bot wysyła po kolei reklamy co parę minut, aż dojdzie do końca. Jeśli ostatnia reklama w kolejce zostanie wysłana, bot znowu zaczyna wysyłać reklamy od początku listy. \n  https://discord.gg/s3J3TwpJh8")
                                    await channel.send(f""" \n \n **REKLAMA PROMOWANA** \n użytkownika: {str(ctx.message.author.name)} / {str(ctx.message.author.id)} \n\n {str(result3)} """)
                                    print(f"{i} -promowanie oferty serwera {ctx.guild.id} przez {ctx.author.id}")
                                    serverListWyslaneOsoby.append(getRandomGuild.name)
                                    print(serverListWyslaneOsoby)
                                except discord.Forbidden:
                                    user = self.client.get_user(318824628439089152)
                                    await user.send(f"Usuń ofertę gildii {getRandomGuild.id}, powód: 'Bot nie może wysłać wiadomości na kanale tekstowym'")
                                    print(f"{i} -promowanie oferty serwera {ctx.guild.id} przez {ctx.author.id}")
                            else:
                                queryDel1 = 'DELETE FROM adversitements WHERE "owner_id" = $1'
                                randomGuild = random.choice(self.client.guilds)
                                getRandomGuild = self.client.get_guild(randomGuild.id)
                                user = self.client.get_user(getRandomGuild.owner_id)
                                try:
                                    embed = discord.Embed(title='Narsty', description='Usunąłem twoją ofertę, ponieważ nie posiadasz kanału do ofert.', color=discord.Color.orange())
                                    await user.send(embed=embed)
                                    await self.client.conn.execute(queryDel1, getRandomGuild.owner_id)
                                except discord.Forbidden:
                                    user = self.client.get_user(318824628439089152)
                                    await user.send(f"Usuń ofertę gildii {getRandomGuild.id}, gdzie właścicielem jest {user.name} / {user.id} powód: 'Bot nie może wysłać wiadomości do właściciela serwera {getRandomGuild}'")
                    separator = ', '
                    x = separator.join(serverListWyslaneOsoby)
                    embed = discord.Embed(title="Narsty", description=f"Serwery, na których została wysłana reklama (jeśli jest mniej niż 10, to znaczy, że te serwery nie mają kanałów tekstowych i związku z tym usunęliśmy ich oferty)) to: {x}", color=discord.Color.orange())
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Narsty", description="Nie masz uprawnień do użycia tej komendy (nie masz dostępu premium)!", color=discord.Color.orange())
                    await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Narsty", description="Nie masz uprawnień do użycia tej komendy (nie jesteś właścicielem serwera)!", color=discord.Color.orange())
            await ctx.send(embed=embed)

    @promuj_oferte.error
    async def command_name_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f"Narsty", description=f"Spokojnie! Wykorzystałeś dzienny limit użyć tej komendy. Spróbuj ponownie za {error.retry_after:.2f} sekund(-/ę/y).", color=discord.Color.orange())
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(promo(client))