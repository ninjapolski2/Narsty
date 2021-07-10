import discord
from discord.ext import commands

class info(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Narsty', description='Komendy: \n **n!kontakt** - informacje o możliwości skontaktowania się ze mną \n **n!socialmedia** - informacje o naszych socialmedia \n **n!projekt** - informacje o projekcie \n **n!donate** - informacje o donate \n **n!premium_oferta** - informacje o dostępie premium \n **n!support** - informacje o supporcie bota \n ***-------------------------------------------------------------------------------------------------*** \n **n!konfiguruj** - TYLKO WŁAŚCICIEL SERWERA - dodaje kanał do wysyłania ofert przez bota \n **n!usun_oferte** - TYLKO WŁAŚCICIEL SERWERA - usuwa ofertę serwerową  \n **n!zaaktualizuj_oferte (treść oferty)** - TYLKO WŁAŚCICIEL BOTA - aktualizuje ofertę \n **n!pokaz_oferte** - TYLKO WŁAŚCICIEL SERWERA - pokazuje ofertę przypisaną do tego serwera \n **n!dodaj_oferte (treść oferty)** - TYLKO WŁAŚCICIEL SERWERA - dodaje ofertę do kolejki na stałe \n **n!kolejkacheck** - TYLKO WŁAŚCICIEL SERWERA - sprawdza, która oferta będzie teraz wyświetlona (numerek zostanie wyświetlony) \n **n!zaaktualizuj_oferte (treść oferty)** - TYLKO WŁAŚCICIEL SERWERA - aktualizuje ofertę \n ***--------------------------------------------------------------------------------------------------*** ', color=discord.Color.orange())
        embed2 = discord.Embed(title='Narsty', description=' ***-------------------------------------------------------------------------------------------------*** \n **n!admin_usun_oferte (ID gildii)** - TYLKO WŁAŚCICIEL BOTA - usuwa ofertę danego serwera  \n **n!admin_daj_premium (ID użytkownika, ID gildii, powód)** - TYLKO WŁAŚCICIEL BOTA - daje użytkownikowi dostęp premium \n **n!admin_zabierz_premium (ID użytkownika, powód)** - TYLKO WŁAŚCICIEL BOTA - zabiera użytkownikowi dostęp premium \n **n!admin_zresetuj_kolejke** - TYLKO WŁAŚCICIEL BOTA - resetuje kolejkę (wraca miejsca nr 1)  \n **n!admin_sprawdz_nr_oferty (ID gildii)** - TYLKO WŁAŚCICIEL BOTA -  sprawdza nr oferty danego serwera \n **n!admin_pokaz_oferte (ID gildii)** - TYLKO WŁAŚCICIEL BOTA - pokazuje daną ofertę  \n **n!admin_nadaj_blackliste (ID użytkownika, ID gildii, powód)** - TYLKO WŁAŚCICIEL BOTA - nadaje blackliste serwerowi \n **n!admin_zabierz_blackliste (ID użytkownika, ID gildii, powód)** - TYLKO WŁAŚCICIEL BOTA - zabiera blackliste serwerowi \n ***-------------------------------------------------------------------------------------------------***', color=discord.Color.orange())
        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)

    @commands.command()
    async def kontakt(self, ctx):
        embed = discord.Embed(title='Narsty', description='Mój Discord: NinjaaaSK#7850 \n E-mail: sebastian.kasprzak556@interia.pl', color=discord.Color.orange())
        await ctx.send(embed=embed)

    @commands.command()
    async def socialmedia(self, ctx):
        embed = discord.Embed(title='Narsty', description='Grupa na Facebooku: https://www.facebook.com/groups/linuxpolska/ \n Kanał na YouTube: https://www.youtube.com/channel/UC8euvc5EIlUp-uLzwUNPaUQ \n Discord LP&TW: https://discord.gg/wAPrHe4 \n Donate: https://tipply.pl/u/narsty-lptw', color=discord.Color.orange())
        await ctx.send(embed=embed)

    @commands.command()
    async def projekt(self, ctx):
        embed = discord.Embed(title='Narsty', description='Współtworzę projekt Linux Polska & Technological World', color=discord.Color.orange())
        await ctx.send(embed=embed)

    @commands.command()
    async def donate(self, ctx):
        embed = discord.Embed(title='Narsty', description='Postaw nam ciastko :) https://tipply.pl/u/narsty-ltpw', color=discord.Color.orange())
        await ctx.send(embed=embed)

    @commands.command()
    async def premium_oferta(self, ctx):
        embed = discord.Embed(title='Narsty', description='Koszt: 15 zł Co daje? Umożliwia tworzenie ekskluzywnych ofert z pingiem everyone lub here. Dzieki temu oferta trafi do o wiele większej liczby odbiorców! Dodatkowo wprowadziłem funckję promowania ofert: na tą chwilę działa to w taki sposób, że oferta zostaje wysyłana do 10 serwerów. Możliwość użycia tej komendy jest 2 razy na 24 godziny.', color=discord.Color.orange())
        await ctx.send(embed=embed)

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(title='Narsty', description='Invite do Discorda supportu bota: https://discord.gg/AHVh3Vvda6', color=discord.Color.orange())
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(info(client))