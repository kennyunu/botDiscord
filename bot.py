import discord
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
WEATHER = os.getenv("OPEN_WEATHER_API")

class MiBot(discord.Client):
    async def on_ready(self):
        print(f"Bot conectado como {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith("!"):
            await self.manejar_comando(message)

    def coordenadas(self, ciudad):
        respuesta = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={ciudad}&limit=1&appid={WEATHER}")
        datos = respuesta.json()
        lat=datos[0]["lat"]
        lon=datos[0]["lon"]
        return lat, lon

    async def manejar_comando(self, message):
        comando = message.content.split()[0].lower()
        argumento = message.content.split()[1:]
        argumento = " ".join(argumento)  # por si la ciudad tiene dos palabras como "Buenos Aires"


        

        if comando == "!hola":
            await message.channel.send(f"Hola {message.author.name}!")
        
        elif comando == "!ayuda":
            await message.channel.send(
                "**Comandos disponibles:**\n"
                "`!hola` — el bot te saluda\n"
                "`!ayuda` — muestra este mensaje\n"
                "`!chiste` — cuenta un chiste en inglés\n"
                "`!trivia` — hace una pregunta en inglés\n"
                "`!dog` — envia una imagen de perrito\n"
                "`!advice` — consejo en inglés\n"
                "`!clima` — descripcion del clima en inglés\n"
            )
        
        elif comando == "!chiste":
            respuesta = requests.get("https://official-joke-api.appspot.com/random_joke")
            datos = respuesta.json()
            await message.channel.send(f"{datos['setup']}\n\n{datos['punchline']}")

        elif comando == "!trivia":
            respuesta = requests.get("https://opentdb.com/api.php?amount=1")
            datos = respuesta.json()
            pregunta = datos['results'][0]
            await message.channel.send(
                f"**Categoría:** {pregunta['category']}\n"
                f"**Dificultad:** {pregunta['difficulty']}\n\n"
                f"**Pregunta:** {pregunta['question']}"
            )
            await message.channel.send(f"||{pregunta['correct_answer']}||")

        elif comando == "!dog":
            respuesta = requests.get("https://dog.ceo/api/breeds/image/random")
            datos = respuesta.json()
            await message.channel.send(f"{datos['message']}\n\n")

        elif comando == "!advice":
            respuesta = requests.get("https://api.adviceslip.com/advice")
            datos = respuesta.json()
            await message.channel.send(f"{datos['slip']['advice']}\n\n")

        elif comando == "!clima":
            lat, lon =self.coordenadas(argumento)
            respuesta = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER}&units=metric")
            datos = respuesta.json()
            descripcion = datos['weather'][0]["description"]
            temp = datos['main']['temp']
            await message.channel.send(
                f"**{argumento}**\n"
                f"🌡️ Temperatura: {temp}°K\n"
                f"☁️ {descripcion.capitalize()}"
            )
        
        else:
            await message.channel.send(f"Comando `{comando}` no reconocido. Escribe `!ayuda`.")

intents = discord.Intents.default()
intents.message_content = True

bot = MiBot(intents=intents)
bot.run(TOKEN)