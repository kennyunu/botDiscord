import discord
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class MiBot(discord.Client):
    async def on_ready(self):
        print(f"Bot conectado como {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith("!"):
            await self.manejar_comando(message)

    async def manejar_comando(self, message):
        comando = message.content.split()[0].lower()

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

        
        else:
            await message.channel.send(f"Comando `{comando}` no reconocido. Escribe `!ayuda`.")

intents = discord.Intents.default()
intents.message_content = True

bot = MiBot(intents=intents)
bot.run(TOKEN)