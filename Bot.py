#discord bot
import discord
import random

"""
def read_token():
        with open("token.txt", "r") as f:
                lines = f.readlines()
                return lines[0].strip()
                """
prefix = "*"
client = discord.Client()
#token = read_token()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == "prefix":
        await message.channel.send("The prefix for this server is:" + prefix)

    elif message.content.startswith((prefix + "stats")):
        e = discord.Embed(title = "https://docs.google.com/spreadsheets/d/1wcDOh-k1beAYH-jv49hdgVCr1unVlj0oSmYyBsjBYSk/edit?usp=sharing")
        await message.channel.send("Here's the stats!", embed = e)
        
    elif message.content.startswith((prefix + "getgud")):
        links = ["https://www.youtube.com/watch?v=bk-1ut6CEb4", "https://www.youtube.com/watch?v=J0DfNsMYXgg", "https://www.youtube.com/watch?v=SuSzet3uJ1E"]
        index = random.randint(0, (len(links) - 1))
        
        e = discord.Embed(title = links[index])
        await message.channel.send("GET GUD SCRUB!", embed = e)
    
    elif message.content.startswith((prefix + "roster")):
        await message.channel.send("""
        @everyone
        Empieza 2:10
        Roster Sabado, Abril 25: \n
        Todo el torneo: Paco, Mango, Nike
        
        
        Tomen foto de las stats despues de cada partida y mandenla a el canal de stats.
        """)
client.run("NzAyODk3NjI5ODE3OTk1MzA0.XqMQ7w.1P_mN9eEviEvkdMfGA5Y6atmv0o")