import requests

respuesta = requests.get("https://api.adviceslip.com/advice")
datos = respuesta.json()
print(datos)