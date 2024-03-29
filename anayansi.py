import subprocess
import sys
import os
import hashlib
from colorama import Fore, Back, Style

def runner(option):
    if os.name == 'nt':
        subprocess.run(["python", f"modules/{option}.py"], shell=True)
    else:
        subprocess.run(["python3", f"modules/{option}.py"])

try:
    print(Fore.LIGHTRED_EX + """
       d8888                                                       d8b
      d88888                                                       Y8P
     d88P888                                                          
    d88P 888 88888b.   8888b.  888  888  8888b.  88888b.  .d8888b  888
   d88P  888 888 "88b     "88b 888  888     "88b 888 "88b 88K      888
  d88P   888 888  888 .d888888 888  888 .d888888 888  888 "Y8888b. 888
 d8888888888 888  888 888  888 Y88b 888 888  888 888  888      X88 888
d88P     888 888  888 "Y888888  "Y88888 "Y888888 888  888  88888P' 888
                                    888                               
                               Y8b d88P                               
                                "Y88P"                                

        Hash Creator & Cracker			[Author : Rawier] """ + Style.RESET_ALL)


except Exception as err:
    pass
print()

while True:
    print(Style.RESET_ALL + "\nMenu:")
    print(Fore.LIGHTGREEN_EX + "1. Hash Cracker")
    print(Fore.LIGHTWHITE_EX + "2. Hash Creator")
    print(Fore.LIGHTRED_EX + "3. Exit" + Style.RESET_ALL)
    op = input("Seleccione una opción: ")

    if op == '1':
        runner("aCracker")
    elif op == '2':
        runner("aCreator")
    elif op == '3':
        print("Exiting the menu...")
        break
    else:
        print(Fore.LIGHTRED_EX + "Invalid option. Please select a valid option.")
