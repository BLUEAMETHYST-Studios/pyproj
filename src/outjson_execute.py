from subprocess import check_output
from colorama import Fore
from sys import exit as kill

def outjson_exec(args):
    try:
        check_output(args) # Using check_output, so that logging is invisible
    except FileNotFoundError:
        print(f"[❌] {Fore.RED}Was not able to build, due to PyInstaller not being installed!")
        kill()
    except Exception:
        print(f"[❌] {Fore.RED}An unknown unexpected Exception occurred!")
        kill()