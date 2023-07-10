from subprocess import run, DEVNULL, STDOUT
from colorama import Fore
from sys import exit as kill

def outjson_exec(args):
    try:
        run(args, stdout=DEVNULL, stderr=STDOUT)
    except FileNotFoundError:
        print(f"[❌] {Fore.RED}Was not able to build, due to PyInstaller not being installed!{Fore.RESET}")
        kill()
    except Exception:
        print(f"[❌] {Fore.RED}An unknown unexpected Exception occurred!{Fore.RESET}")
        kill()