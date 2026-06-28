actions = {
    "play": ["play", "start", "begin", "run"],
    "open": ["open", "launch"],
    "search": ["search", "find", "look", "check"],
    "tell" : ["say", "tell"]
}
targets = {
    "music",
    "spotify",
    "youtube",
    "time"
}

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
        for key in actions:
            if word in actions[key]:
                action = key
                break  

        if word in targets:
            target = word
    return action, target


