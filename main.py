from commands import play_music
from commands import open_spotify
from commands import search_youtube
from commands import tell_time
from commands import exit_program
from commands import parse_command

running = True


command_map = {
    ("play", "music"): play_music,
    ("open", "spotify"): open_spotify,
    ("search", "youtube"): search_youtube,
    ("tell", "time"): tell_time,
}

while running:
    commands = input("What can I do for you?")
    commands = commands.strip().lower().split()

    action, target = parse_command(commands)
    
    command_key = (action, target)
    
    if command_key in command_map:
        action_function = command_map[command_key]
        result = action_function()

        if result == False:
            running = False 
    
    else:
        print("Command not found!")
        
        


        



    




