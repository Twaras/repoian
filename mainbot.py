from discord import File, Embed
import discord
from config import TOKEN #el archivo config.py debe tener un .gitignore, contiene la variable TOKEN = "aaaaaaaaaaaaaaaa"

client = discord.Client()

@client.event
async def on_ready(): # se ejecuta cada vez que el bot se inicia
    print("on ready...")
    #define la actividad listening to "ayudian" mediante el metodo change_presence 
    listening = discord.Activity(type=discord.ActivityType.listening, name="ayudian")
    await client.change_presence(activity=listening)

    channel = client.get_channel(765797769750642731) #obtiene el canal general según la id, hay que copiarla directamente por ahora
    #await channel.send("E LET´S GOOOO!")

@client.event
async def on_message(mensaje):

    #evita leer los mensajes propios
    if(mensaje.author == client.user):
        return
    
    #comando sexo
    if mensaje.content.startswith("sexo"):
        #envía el mensaje "SEXOOOO..."
        #await mensaje.channel.send(file=File("./melons.jpg"))
        await mensaje.channel.send("SEXOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")

    #comando ian
    if mensaje.content.startswith("ian"):
        #envía la foto del ian "aaa.jpg"
        await mensaje.channel.send(file=File("./aaa.jpg"))

    #comando ayudian
    if mensaje.content.startswith("ayudian"):
        #crea un mensaje embed con la lista de comandos
        embed = Embed(title="Comandos")

        #lista de comandos -> ("comando","descripcion","False")
        fields = [("sexo","SEXOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!", False),
                  ("ian","foto del ian", False)]
        for name,value,inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await mensaje.channel.send(embed=embed)

#usa el token para ejecutar el bot
client.run(TOKEN)