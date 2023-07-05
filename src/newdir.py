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
        print(f"{Fore.RED}[ERROR] Folder with the name {name} already exists!{Fore.RESET}")
        kill()
    except Exception:
        print(f"{Fore.RED}[ERROR] Folder can't be created!{Fore.RESET}")
        kill()