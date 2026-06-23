from commands import greet_user
from commands import play_music
from commands import open_spotify
from commands import exit_program

running = True
command_map = {
    "hello": greet_user,
    "play music": play_music,
    "open spotify": open_spotify,
    "exit program": exit_program
}

while running:
    commands = input("What can I do for you?")
    commands = commands.strip().lower()
    if commands in command_map:
        action = command_map[commands]
        result = action()
        if result == False:
            running = False
        else:
            running = True
    else:
        print("command not found")

    




