

def process_command(command):

  if command == "hello":
    print("Hey, I'm Jarvis!")
    return True
  elif command == "play music":
    print("Playing music...")
    return True
  elif command == "open spotify":
    print("Opening Spotify...")
    return True
  elif command == "exit":
    print("GoodBye!")
    return False
  else:
    print("I didn't understand")
    return True
 
running = True

while running:
  command = input("Hey, what could i do for you? ")
  command = command.strip().lower()
  running = process_command(command)
  

