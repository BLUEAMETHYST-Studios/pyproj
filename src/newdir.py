from os import mkdir, chdir
from colorama import Fore, init
from sys import exit as kill

init()

def newdir(name):
    print("Creating new directory ...")
    try:
        mkdir(name)
        chdir(name)
    except FileExistsError:
        print(f"[❌] {Fore.RED}Folder with the name {Fore.CYAN}{name}{Fore.RED} already exists!{Fore.RESET}")
        kill()
    except Exception:
        print(f"[❌] {Fore.RED}Folder can't be created!{Fore.RESET}")
        kill()