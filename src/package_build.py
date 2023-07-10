from subprocess import run, DEVNULL, STDOUT
from platform import system
from colorama import Fore
from sys import exit as kill
from time import time

start = time()

try:
    print("Building package ...")
    if system() == "Windows":
        run(["python", "setup.py", "bdist_wheel"], stdout=DEVNULL, stderr=STDOUT)
    else:
        run(["python3", "setup.py", "bdist_wheel"], stdout=DEVNULL, stderr=STDOUT)
except Exception:
    print(f"[❌] {Fore.RED}An unknown unexpected exception occurred!{Fore.RESET}")
    kill()
else:
    print(f"[✅] Package building process {Fore.GREEN}completed{Fore.RESET} within {Fore.CYAN}{time() - start:.2f}{Fore.RESET} seconds!")