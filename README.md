# Bot de Discord

Bot de Discord desarrollado en Python con múltiples comandos y consumo de APIs externas.

## Comandos

| Comando | Descripción |
|---|---|
| `!hola` | El bot te saluda |
| `!ayuda` | Muestra los comandos disponibles |
| `!chiste` | Cuenta un chiste aleatorio |
| `!trivia` | Pregunta de trivia aleatoria |
| `!dog` | Envía una foto aleatoria de un perro |
| `!advice` | Consejo aleatorio |
| `!clima [ciudad]` | Muestra el clima actual de una ciudad |

## Tecnologías

- Python 3
- discord.py 2.7.1
- APIs: OpenWeatherMap, Open Trivia DB, dog.ceo, Advice Slip, Official Joke API

## Instalación

1. Clona el repositorio
2. Instala las dependencias: 
    pip install discord.py requests python-dotenv
3. Crea un archivo `.env` con:
    DISCORD_TOKEN=tu_token_aquí
    OPEN_WEATHER_API=tu_api_key_aquí
4. Ejecuta el bot:
    python bot.py
