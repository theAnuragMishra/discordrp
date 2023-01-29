from pypresence import Presence # The simple rich presence client in pypresence
import time
import os
from dotenv import load_dotenv

load_dotenv()
application_id = os.getenv('APPLICATION_ID')

client_id = 1069249925994524783  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect()  # Start the handshake loop

RPC.update(state="Rich Presence using pypresence!") # Updates our presence
t = int(time.time())
while True:  # The presence will stay on as long as the program is running
    RPC.update(
        large_image="cengage",
        large_text="Practising calculus problems",
        details="From Cengage",
        state="Relations & Functions",
        start=t,
        buttons=[{"label":"Join me!","url":"https://discord.gg/er5QD69vqV"}]
    )
    time.sleep(60)
