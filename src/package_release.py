from subprocess import run, DEVNULL, STDOUT
from colorama import Fore
from sys import exit as kill
from time import time

from secrettemplate import secrettemplate
from package_release_parse import parse

start = time()

try:
    secretsjson = open("secrets.json", "r")
    secrets = secretsjson.read()
    secretsjson.close()
except FileNotFoundError:
    try:
        print(f"[❌] {Fore.RED}secrets.json file doesn't exist!{Fore.RESET}")
        print("Creating a new secrets.json file ...")
        new_secrets = open("secrets.json", "w")
        new_secrets.write(secrettemplate)
        new_secrets.close()
    except Exception:
        print(f"[❌] {Fore.RED}Not able to create new secrets.json!{Fore.RESET}")
        kill()
    else:
        print(f"[✅] A new secrets.json file was created, be sure to set the values correctly!")
        kill()
else:
    secretjson = parse(secrets)
    try:
        print("Uploading ...")
        run(["twine", "upload", "dist/*", "-p", secretjson[0], "-u", secretjson[1]], stdout=DEVNULL, stderr=STDOUT)
    except Exception:
        print(f"[❌] {Fore.RED}Upload failed!{Fore.RESET}")
    else:
        print(f"[✅] Upload {Fore.GREEN}completed{Fore.RESET} within {Fore.CYAN}{time() - start:.2f}{Fore.RESET} seconds!")