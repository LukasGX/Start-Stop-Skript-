import os

def runCommand(command):
    global directory
    if (command.startswith("lul")):
        for i in range(5):
            print("gg")
    elif (command.startswith("ls")):
        print("Listing files...")
        os.system("dir")
    elif (command.startswith("cd")):
        path = command[3:].strip()
        if os.path.exists(path):
            os.chdir(path)
            directory = os.getcwd()
            print(f"Changed directory to {path}")
        else:
            print(f"Directory {path} does not exist.")
    elif (command.startswith("cat")):
        filename = command[4:].strip()
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
    elif (command.startswith("exit")):
        print("Exiting...")
        exit()

directory = os.getcwd()

print("==============================================================")
print("Select option:")
print("1) Start")
print("2) Exit")
print("==============================================================")
user_input = ""
try:
    user_input = str(input("Your option: "))
except KeyboardInterrupt:
    print("")
if user_input == "1":
    if not os.name == 'nt':
        print("Not Running on Windows! Exiting...")
        exit()
    while True:
        try:
            user_command = str(input(f"({directory}) >> "))
            runCommand(user_command)
        except KeyboardInterrupt:
            print("Use 'exit' command to quit.")
elif user_input == "2":
    print("Exiting...")
    exit()
else:
    print("Unknown input!")