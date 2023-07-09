from outjson_parse import *
from outjson_check import *
from outjson_execute import *

from colorama import *
from sys import exit as kill
from time import time

start = time()

try:
    jfile = open("out.json", "r")
    jfile = jfile.read()
except FileNotFoundError:
    print(f"[❌] {Fore.RED}Was not able to find out.json file!{Fore.RESET}")
    kill()
except UnicodeDecodeError:
    print(f"[❌] {Fore.RED}The out.json file includes unreadable characters!{Fore.RESET}")
    kill()
except Exception:
    print(f"[❌] {Fore.RED}An unknown and unexpected exception occurred!{Fore.RESET}")

print("Checking JSON file ...")
check_json(jfile)
print("Parsing JSON file ...")
startargs = parsejson(jfile)
print("Building ...")
outjson_exec(startargs)
print(f"[✅] Building process {Fore.GREEN}completed{Fore.RESET} in {Fore.CYAN}{time() - start:.2f}{Fore.RESET} seconds!")
