import time
import os

try:
    from pypresence import Presence
    from dotenv import load_dotenv
    from InquirerPy import prompt
    from colorama import init, Fore
except ImportError:
    os.system("pip install pypresence python-dotenv InquirerPy colorama")
    from pypresence import Presence
    from dotenv import load_dotenv
    from InquirerPy import prompt
    from colorama import init, Fore

init(autoreset=True)
def clsr(): return os.system('cls' if os.name == 'nt' else 'clear')


clsr()

load_dotenv()
application_id = os.getenv('APPLICATION_ID')

client_id = 1069249925994524783  # Put your Client ID in here


def textart():
    clsr()
    print(f"""
{Fore.RED}     _  _____  _____      _     ____  __     __  ____    ___   ____   _____ 
{Fore.RED}    | || ____|| ____|    / \   |  _ \ \ \   / / |___ \  / _ \ |___ \ |___ / 
{Fore.WHITE}    | ||  _|  |  _|     / _ \  | | | | \ \ / /    __) || | | |  __) |  |_ \ 
{Fore.GREEN}| |_| || |___ | |___   / ___ \ | |_| |  \ V /    / __/ | |_| | / __/  ___) |
{Fore.GREEN} \___/ |_____||_____| /_/   \_\|____/    \_/    |_____| \___/ |_____||____/ 
 
 {Fore.WHITE} ----------
 {Fore.BLUE} Version: 1.0.2
 {Fore.RED} Developer: Anurag Mishra
 {Fore.CYAN} Discord: Anurag#2993
    """)


textart()

design = {
    "questionmark": "#3FD536 bold",
    "question": "#CB2B39 bold",
    "pointer": "#2381C9",
    "answer": "#C9C918"
}
t = int(time.time())


def rpcData():
    textart()
    dataIn = [
        {
            "type": "list",
            "name": "subject",
            "message": "Select what you're doing",
            "choices": ['CATS','CHAMP','HCV', 'Cengage', 'Marks', 'PW Modules', 'N Avasthi', 'MS Chauhan']
        },
        {
            "type": "input",
            "name": "topic",
            "message": "What topic are you studying: ",
            "validate": lambda res: len(res) > 0,
            "invalid_message": "Input cannot be empty."
        },

        {
            "type": "list",
            "name": "torp",
            "message": "Are you studying theory or doing practice?",
            "choices": ["Studying Theory", "Practising"]
        }

    ]
    data = prompt(dataIn, style=design)
    if data['torp'].startswith('Studying'):
        return data['subject'], data['topic'], "Studying Theory"
    else:
        return data['subject'], data['topic'], "Practising"


RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect()  # Start the handshake loop


def update_presence():
    data = rpcData()
    try:
        RPC.clear()
    except Exception:
        RPC.connect()  # This means that the connection already got disconnected, so attempt to start a new one
    if data[0] == "PW Modules":
        large_image = "pwm"
    elif data[0] == "N Avasthi":
        large_image = "na"
    elif data[0] == "MS Chauhan":
        large_image = "mschauhan"
    elif data[0] == "CATS":
        large_image = "cats"
    elif data[0] == "CHAMP":
        large_image = "champ"
    else:
        large_image = data[0].lower()
    large_text = data[0].title()

    RPC.update(
        state=data[1].title(),
        details=f"{data[2].title()} from {data[0]}",
        start=t,
        large_image=large_image,
        large_text=large_text,
        buttons=[{"label": "Join me in studying!",
                  "url": "https://discord.gg/er5QD69vqV"}]
    )
    print(f"{Fore.BLUE} >>> Rich Presence Updated!")
    print(
        f"{Fore.CYAN} >>> Leave this window open until you want to quit rich presence, you can keep it minimised")


while True:
    print("\n")
    data = prompt({"type": "list", "name": "dat", "message": "What do you want to do?",
                   "choices": ["Update rich presence", "Close"]}, style=design)
    if data['dat'] == "Update rich presence":
        update_presence()
    else:
        try:
            RPC.close()
        except Exception:
            pass
        print(f"{Fore.GREEN} >>> Rich Presence closed!")
        break
