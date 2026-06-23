from commands import play_music
from commands import open_spotify
from commands import search_youtube
from commands import tell_time
from commands import exit_program

running = True

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

command_map = {
    ("play", "music"): play_music,
    ("open", "spotify"): open_spotify,
    ("search", "youtube"): search_youtube,
    ("tell", "time"): tell_time,
}

while running:
    action = None
    target = None
    commands = input("What can I do for you?")
    commands = commands.strip().lower().split()
    for word in commands:
        if word in actions:
            action = word
        if word in targets:
            target = word
    command_key = (action, target)
    if command_key in command_map:
        action_function = command_map[command_key]
        result = action_function()

        if result == False:
            running = False 
    
    else:
        print("Command not found!")
        

        



    




