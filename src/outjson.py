from json import loads, JSONDecodeError
from colorama import Fore
from sys import exit as kill
from subprocess import run, CalledProcessError
from time import time

def parse_and_make():
    start = time()


    try:
        file = loads(open("out.json", "r").read())
    except FileNotFoundError:
        print(f"{Fore.RED}Not able to find out.json configuration file.")
        kill()
    except JSONDecodeError:
        print(f"{Fore.RED}Invalid JSON!")
        kill()

    if not isinstance(file, list):
        print(f"{Fore.RED}out.json file must provide arguments as a list!")
        kill()

    try:
        run(file)
    except FileNotFoundError:
        print(f"{Fore.RED}out.json provides a command that doesn't exist")
    except CalledProcessError:
        print(f"{Fore.RED}out.json file provides a command, that seems to exist, but it failed!")
    else:
        print(f"Building process completed within {time() - start:.2f} seconds!")