from discord import File
import discord
from config import TOKEN #el archivo config.py debe tener un .gitignore, contiene la variable TOKEN = "aaaaaaaaaaaaaaaa"

client = discord.Client()

@client.event
async def on_ready(): # se ejecuta cada vez que el bot se inicia
    print("aaaaaaa")
    channel = client.get_channel(765797769750642731) #obtiene el canal general según la id, hay que copiarla directamente por ahora
    await channel.send("E LET´S GOOOO!")

@client.event
async def on_message(mensaje):

    #evita leer los mensajes propios
    if(mensaje.author == client.user):
        return
    
    #comando sexo
    if mensaje.content.startswith("sexo"):
        await mensaje.channel.send(file=File("./melons.jpg"))
        await mensaje.channel.send("SEXOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")

    #comando ian
    if mensaje.content.startswith("ian"):
        #await mensaje.channel.send("hola we")
        await mensaje.channel.send(file=File("./aaa.jpg"))

#usa el token 
client.run(TOKEN)