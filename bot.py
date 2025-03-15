import discord
import passive


#bot tokenMTM1MDQ3NTk2NDYwOTQ2MjM3NA.G3YbZt.bxn3B8sZQP3BZuavDCKOocxGoGMTssyudm5HoI
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$Void'):
        await message.channel.send("https://youtu.be/gU38Wk24inM?si=fipMPOxPboHKWeJS")
    else:
        await message.channel.send(message.content)

client.run("token")
