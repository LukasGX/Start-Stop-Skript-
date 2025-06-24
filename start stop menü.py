import os

def runCommand(command):
 if (command.startsWith("lul")):
  for i in range(5):
   print("gg")

print("==============================================================\n")
print("Select option: \n")
print("1)Start\n")
print("2)Exit\n")
user_input = str(input("Your option: "))
if user_input == "1":
 user_command = str(input("Insert command: "))
 runCommand(user_command)

elif user_input == "2":
    exit()
else:
    print('Unknown input!\n')
