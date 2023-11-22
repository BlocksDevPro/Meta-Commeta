import config
from pyrogram import Client
from handlers.channel import registerHandlers

print("Creating the client...")
client = Client(config.PHONE_NUMBER, config.API_ID,
                config.API_HASH, phone_number=config.PHONE_NUMBER)

print("Registering post handlers...")
registerHandlers(client)

print("Starting the client...")
client.run()
