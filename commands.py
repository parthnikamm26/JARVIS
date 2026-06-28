actions = [
    "play",
    "open",
    "search",
    "tell"
]

targets = [
    "music",
    "spotify",
    "youtube",
    "time"
]

def play_music():
    print("Playing music...")

def open_spotify():
    print("Opening Spotify...")
   
def search_youtube():
    print("Searching Youtube...")

def tell_time():
    print("The time is...")

def exit_program():
    print("GOODBYE!")
    return False

def parse_command(commands):
    action = None
    target = None

    for word in commands:
        if word in actions:
            action = word
        if word in targets:
            target = word
    return action, target


