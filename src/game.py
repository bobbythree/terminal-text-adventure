import pyfiglet
import player
from verbs import *
from one_word_commands import *
from scenes import bedroom, street

# text-parser funcs
def command_prompt(scene_name):
    """display the command prompt in current scene. tokenize user input.
    loop over tokens. put verbs, nouns etc into command_list. Call 
    run_command func, passing it the commands"""
    command = input("> ")
    tokens = command.lower().split()
    command_list = []
    for x in tokens:       
        if x in verbs.keys() and x not in command_list:
            command_list.append(x)
        elif x in scene_name.scene["nouns"].keys() and x not in command_list:
            command_list.append(x)
        elif x in player.stats["inventory"].values() and x not in command_list:
            command_list.append(x)       
    
    run_command(command_list, scene_name)

def run_command(command, scene_name):
    """take in command list and current scene name. handle various commands
    and errors. If no errors, execute the verb function from verbs.py. Call the 
    command_prompt func again."""
    if command == []: # if no words matched known words
        print("does not compute.")
    if command[0] == "exit": # if verb is "exit"
        next_scene = scene_name.scene["nouns"][command[1]]["next_scene"]
        print(f"you exit the {command[1]}")
        command_prompt(next_scene)        
    elif command[0] in verbs.keys() and len(command) == 1: # if no noun
        print(f"{command[0]}...?")
    elif command[0] in verbs.keys() and command[1] not in scene_name.scene["nouns"].keys() and command[1] in player.stats["inventory"].values(): # if item is in inventory, not scene
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)
    elif command[0] not in verbs.keys() or command[1] not in scene_name.scene["nouns"].keys(): # if either verb or noun missing
        print("try saying that another way.")    
    elif command[0] in verbs.keys() and command[1] in scene_name.scene["nouns"].keys(): # both verb and noun match
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)
    
    
    #loop back into the prompt
    command_prompt(scene_name)

# start of gameplay
def start():
    """display welcome message. Call command_prompt func with first scene."""
    game_logo = pyfiglet.figlet_format("Q U E S T", font="colossal")
    print(game_logo)
    print("""Welcome to QUEST! You wake up in your bedroom which is dimly lit by artificial light coming through the [window]. In the room is your [computer] sitting on a [desk]. There is one [door] to get out.""")            

if __name__ == "__main__":
    start()

#initial call 
command_prompt(bedroom)  


