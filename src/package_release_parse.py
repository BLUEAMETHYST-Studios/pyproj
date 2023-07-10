from json import loads
from colorama import Fore
from sys import exit as kill

def parse(json):
    try:
        j = loads(json)
        return [j["username"], j["password"]]
    except KeyError:
        print(f"[❌] {Fore.RED}Invalid JSON format in secrets.json!{Fore.RESET}")
        kill()