#!usr/bin/env python
# Author : Rawier
import hashlib
from colorama import Fore, Back, Style

try:
    print(Fore.GREEN + """         
██╗  ██╗ █████╗ ███████╗██╗  ██╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║███████║███████╗███████║    ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██╔══██║╚════██║██╔══██║    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║███████║██║  ██║    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

            Hash Cracker			[Author : Rawier] """ + Style.RESET_ALL)

except Exception as err:
    pass
print()


def sha512():
    """ SHA512 is for Decrypting Raw SHA512 Hash"""
    hash = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter the Hash : " + Fore.GREEN)
    w_list = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Input Full Path of Wordlist : " + Fore.GREEN)
    print(Style.RESET_ALL)
    pass_file = open(w_list, "r")

    for i in pass_file:
        file_enc = i.encode('utf-8')
        md_hash = hashlib.sha512(file_enc.strip()).hexdigest()

        if md_hash == hash:
            print(Fore.GREEN + " Password Found :", i + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + " Password Not Found !!!" + Style.RESET_ALL)


def sha256():
    """ SHA256 is for Decrypting Raw SHA256 Hash"""
    hash = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter the Hash : " + Fore.GREEN)
    w_list = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Input Full Path of Wordlist : " + Fore.GREEN)
    print(Style.RESET_ALL)
    pass_file = open(w_list, "r")

    for i in pass_file:
        file_enc = i.encode('utf-8')
        md_hash = hashlib.sha256(file_enc.strip()).hexdigest()

        if md_hash == hash:
            print(Fore.GREEN + " Password Found :", i + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + " Password Not Found !!!" + Style.RESET_ALL)


def sha384():
    """ SHA1 is for Decrypting Raw SHA1 Hash"""
    hash = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter the Hash : " + Fore.GREEN)
    w_list = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Input Full Path of Wordlist : " + Fore.GREEN)
    print(Style.RESET_ALL)
    pass_file = open(w_list, "r")

    for i in pass_file:
        file_enc = i.encode('utf-8')
        md_hash = hashlib.sha384(file_enc.strip()).hexdigest()

        if md_hash == hash:
            print(Fore.GREEN + " Password Found :", i + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + " Password Not Found !!!" + Style.RESET_ALL)


def md5():
    """ MD5 is for Decrypting Raw MD5 Hash"""
    hash = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter the Hash : " + Fore.GREEN)
    w_list = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Input Full Path of Wordlist : " + Fore.GREEN)
    print(Style.RESET_ALL)
    pass_file = open(w_list, "r")

    for i in pass_file:
        file_enc = i.encode('utf-8')
        md_hash = hashlib.md5(file_enc.strip()).hexdigest()

        if md_hash == hash:
            print(Fore.GREEN + " Password Found :", i + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + " Password Not Found !!!" + Style.RESET_ALL)


def sha1():
    """ SHA1 is for Decrypting Raw SHA1 Hash"""
    hash = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter the Hash : " + Fore.GREEN)
    w_list = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Input Full Path of Wordlist : " + Fore.GREEN)
    print(Style.RESET_ALL)
    pass_file = open(w_list, "r")

    for i in pass_file:
        file_enc = i.encode('utf-8')
        md_hash = hashlib.sha1(file_enc.strip()).hexdigest()

        if md_hash == hash:
            print(Fore.GREEN + " Password Found :", i + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + " Password Not Found !!!" + Style.RESET_ALL)

def blake2():
    """ SHA1 is for Decrypting Raw SHA1 Hash"""
    hash = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter the Hash : " + Fore.GREEN)
    w_list = input(
        Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Input Full Path of Wordlist : " + Fore.GREEN)
    print(Style.RESET_ALL)
    pass_file = open(w_list, "r")

    for i in pass_file:
        file_enc = i.encode('utf-8')
        md_hash = hashlib.blake2b(file_enc.strip()).hexdigest()

        if md_hash == hash:
            print(Fore.GREEN + " Password Found :", i + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + " Password Not Found !!!" + Style.RESET_ALL)

ex = 'n'
while ex != 'y':
    try:
        print(""" Choose Following Options For Hash Type :  
         1 : MD5
         2 : SHA1
         3 : SHA256
         4 : SHA384
         5 : SHA512""")
        op = int(input(" Enter Options : "))
        print()
        if op == 1:
            print(md5())
        elif op == 2:
            print(sha1())
        elif op == 3:
            print(sha256())
        elif op == 4:
            print(sha384())
        elif op == 5:
            print(sha512())
        else:
            print("\t Wrong Input...\t Exiting Program...")
    except Exception as error:
        print(f"\n {error} \n\t Error Encountered...")
        pass
    ex = input(" Do You Want to Exit ? [y,n] : ")
    if ex == 'y':
        print("  Ending... :)")
    print()
    continue

