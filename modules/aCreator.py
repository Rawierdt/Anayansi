#!usr/bin/env python
import hashlib
from colorama import Fore, Style
print(Fore.LIGHTWHITE_EX + """    __  __           __            
░█░█░█▀█░█▀▀░█░█░░░█▀▀░█▀▄░█▀▀░█▀█░▀█▀░█▀█░█▀▄
░█▀█░█▀█░▀▀█░█▀█░░░█░░░█▀▄░█▀▀░█▀█░░█░░█░█░█▀▄
░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀

    Hash Creator			[Author : Rawier] """ + Style.RESET_ALL)


def md5():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    md5 = hashlib.md5(text.encode('utf8').strip()).hexdigest()
    print(f"\n MD5 Hash : {Fore.GREEN}{md5}{Style.RESET_ALL}\n")


def sha1():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    sha1 = hashlib.sha1(text.encode('utf8').strip()).hexdigest()
    print(f"\n SHA1 Hash : {Fore.GREEN}{sha1}{Style.RESET_ALL}\n")


def sha256():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    sha256 = hashlib.sha256(text.encode('utf8').strip()).hexdigest()
    print(f"\n SHA256 Hash : {Fore.GREEN}{sha256}{Style.RESET_ALL}\n")


def sha384():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    sha384 = hashlib.sha384(text.encode('utf8').strip()).hexdigest()
    print(f"\n SHA384 Hash : {Fore.GREEN}{sha384}{Style.RESET_ALL}\n")


def sha512():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    sha512 = hashlib.sha512(text.encode('utf8').strip()).hexdigest()
    print(f"\n SHA512 Hash : {Fore.GREEN}{sha512}{Style.RESET_ALL}\n")


ex = 'n'
while ex != 'y':
    try:
        print()
        print(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Choose "
                                                                                        "option for Generating Hash : ")
        print("""     \t 1 : MD5
         2 : SHA1
         3 : SHA256
         4 : SHA384
         5 : SHA512""")
        op = int(input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter Option : " + Fore.GREEN + Style.RESET_ALL))
        print()
        if op == 1:
            md5()
        elif op == 2:
            sha1()
        elif op == 3:
            sha256()
        elif op == 4:
            sha384()
        elif op == 5:
            sha512()
        else:
            print(" Wrong Input !!!")
    except Exception as error:
        print(f"\n {error}\n  Error Encountered...\t Exiting Program...")
    ex = input(" Do You Want to Exit [y,n] ? : ")
    if ex == 'y':
        print("\n Thank You for Using this Program...")
        print()
    continue
