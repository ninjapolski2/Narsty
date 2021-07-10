import random
import discord
from discord.ext import commands, tasks

class looptasks(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.oferty_wysylanie = self.oferty_wysylanie
        self.oferty_wysylanie.start()

    def cog_unload(self):
        self.oferty_wysylanie = self.oferty_wysylanie
        self.oferty_wysylanie.cancel()

    @tasks.loop(seconds=15.0)
    async def oferty_wysylanie(self):
        print("Start")
        for guild in self.client.guilds:
            randomChannel = random.choice(self.client.guilds)
            randomChannelGuild = self.client.get_guild(randomChannel.id)
            if '🔔narsty' in [c.name for c in randomChannelGuild.text_channels]:
                query1 = 'SELECT "queue_number" FROM adv_queue'
                result1 = await self.client.conn.fetchval(query1)
                query2 = 'SELECT "owner_id", row_num FROM (SELECT *, ROW_NUMBER() OVER() AS row_num FROM adversitements) result WHERE row_num = $1'
                query3 = 'SELECT "adv_description", row_num FROM (SELECT *, ROW_NUMBER() OVER() AS row_num FROM adversitements) result WHERE row_num = $1'
                query4 = 'SELECT COUNT("adv_description") FROM adversitements'
                result2 = await self.client.conn.fetchval(query2, result1)
                result3 = await self.client.conn.fetchval(query3, result1)
                result4 = await self.client.conn.fetchval(query4)
                if result1 % 5 == 0:
                    query5 = 'SELECT "queue_number" FROM adv_queue'
                    result5 = await self.client.conn.fetchval(query5)
                    queryUpdate1 = 'UPDATE adv_queue SET "queue_number" = ($1 + 1)'
                    randomChannel = random.choice(self.client.guilds)
                    randomChannelGuild = self.client.get_guild(randomChannel.id)
                    channel = discord.utils.find(lambda r: r.name == '🔔narsty', randomChannelGuild.text_channels)
                    if channel is not None:
                        try:
                            await channel.send("Użytkowniku, zapewne nie raz chciałeś jakoś zarobić, posiadając umiejętności, ale nie wiesz jak się zareklamować lub wypromować?💰💰💰 \n Nasz bot ***NinjaPortal*** oferuje reklamowanie ciebie w zakresie: \n▫ kupię 💵 \n ▫ sprzedam 💵 \n ▫ wymienię się 💵 \n ▫ robię 💵 \n ▫ potrzebuję 💵 \n ▫ szukam (kogoś, czegoś) 💵 \n itp... \n Co trzeba spełnić, żeby twoja oferta znalazła się w kolejce?: \n ▫ dodać naszego bota, który będzie reklamował innych oferty na twoim serwerze \n ▫ stworzyć kanał :bell:ninjaportal z uprawnieniami wysyłania wiadomości tylko przez bota oraz możliwość wysyłania wzmianek everyone i here (bot samodzielnie doda kanał, lecz w razie potrzeby stworzyłem specjalną komendę do utworzenia) \n ▫ zapoznaj się z komendami za pomocą komendy n!help \n ▫ zapoznaj się z regulaminem, żebyś nie dostał blacklisty na twój serwer i twoje konto! \n Jak bot działa? \n ▪ Zostajesz zapisany do kolejki, gdzie reklamy są wysyłane co jakiś czas. Bot wysyła po kolei reklamy co parę minut, aż dojdzie do końca. Jeśli ostatnia reklama w kolejce zostanie wysłana, bot znowu zaczyna wysyłać reklamy od początku listy. \n  https://discord.gg/muYh7Harwx")
                            await self.client.conn.execute(queryUpdate1, result5)
                            print(".ofertaTwórcy")
                        except discord.Forbidden:
                            user = self.client.get_user(318824628439089152)
                            await user.send(f"Usuń ofertę gildii {randomChannelGuild.id}, gdzie właściciel to {randomChannelGuild.owner_id}, powód: 'Bot nie może wysłać wiadomości na kanale tekstowym'")
                            print(".nieudaneWysłanieWiadomości1")
                    else:
                        queryDel1 = 'DELETE FROM adversitements WHERE "owner_id" = $1'
                        randomChannel = random.choice(self.client.guilds)
                        randomChannelGuild = self.client.get_guild(randomChannel.id)
                        user = await self.client.get_user(randomChannelGuild.owner_id)
                        try:
                            embed = discord.Embed(title='Narsty', description=f'Usunąłem twoją ofertę, ponieważ nie posiadasz kanału do ofert. Serwer: {randomChannelGuild.name} [1]', color=discord.Color.orange())
                            await user.send(embed=embed)
                            await self.client.conn.execute(queryDel1, randomChannelGuild.owner_id)
                            print(".brakKanału1")
                        except discord.Forbidden:
                            user = self.client.get_user(318824628439089152)
                            await user.send(f"Usuń ofertę gildii {randomChannelGuild.id}, gdzie właściciel to {randomChannelGuild.owner_id}, powód: 'Bot nie może wysłać wiadomości do właściciela serwera {randomChannelGuild}'")
                            print(".nieudaneWysłanieWiadomości2")
                elif result1 <= result4:
                    randomChannel = random.choice(self.client.guilds)
                    randomChannelGuild = self.client.get_guild(randomChannel.id)
                    channel = discord.utils.find(lambda r: r.name == '🔔narsty', randomChannelGuild.text_channels)
                    if channel is not None:
                        queryUpdate2 = 'UPDATE adv_queue SET "queue_number" = ($1 + 1)'
                        query6 = 'SELECT "queue_number" FROM adv_queue'
                        result6 = await self.client.conn.fetchval(query6)
                        print(".updateKolejki1")
                        try:
                            await channel.send(f"=-=-=-=\n Oferta właściciela: {result2} \n\n {result3} \n =-=-=-=")
                            await self.client.conn.execute(queryUpdate2, result6)
                            print(".udanaOferta")
                        except discord.Forbidden:
                            user = self.client.get_user(318824628439089152)
                            await user.send(f"Usuń ofertę gildii {randomChannelGuild.id}, gdzie właściciel to {randomChannelGuild.owner_id}, powód: 'Bot nie może wysłać wiadomości na kanale tekstowym {randomChannelGuild}'")
                            print(".nieudaneWysłanieWiadomości3")
                    else:
                        queryDel2 = 'DELETE FROM adversitements WHERE "owner_id" = $1'
                        await self.client.conn.execute(queryDel2, randomChannelGuild.owner_id)
                        user = self.client.get_user(randomChannelGuild.owner_id)
                        try:
                            embed = discord.Embed(title='Narsty', description=f'Usunąłem twoją ofertę, ponieważ nie posiadasz kanału do ofert. Serwer: {randomChannelGuild.name} [2]', color=discord.Color.orange())
                            await user.send(embed=embed)
                            print(".brakKanału2")
                        except discord.Forbidden:
                            user = self.client.get_user(318824628439089152)
                            await user.send(f"Usuń ofertę gildii {randomChannelGuild.id}, gdzie właściciel to {randomChannelGuild.owner_id}, powód: 'Bot nie może wysłać wiadomości do właściciela serwera {randomChannelGuild}'")
                            print(".nieudaneWysłanieWiadomości4")
                elif result1 > result4:
                    queryUpdate3 = 'UPDATE adv_queue SET "queue_number" = 1'
                    await self.client.conn.execute(queryUpdate3)
                    print(".updateKolejki2")
                    break
            else:
                query7 = 'SELECT "guild_id", "owner_id", "adv_description" FROM adversitements WHERE "guild_id" = $1'
                result7 = await self.client.conn.fetchval(query7, randomChannelGuild.id)
                if result7:
                    queryDel3 = 'DELETE FROM adversitements WHERE "guild_id" = $1'
                    await self.client.conn.execute(queryDel3, randomChannelGuild.id)

        print("Koniec")


    @oferty_wysylanie.before_loop
    async def before_printer(self):
        print('Czekanie...')
        await self.client.wait_until_ready()


def setup(client):
    client.add_cog(looptasks(client))